import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from flask import Flask, redirect, url_for, render_template, request, session, abort, jsonify
from flask_dance.contrib.github import make_github_blueprint, github
from flask_wtf.csrf import CSRFProtect, validate_csrf
from termcolor import cprint

from py_tools import *

app = Flask(__name__)
csrfp = CSRFProtect(app)
app.config['UPLOAD_FOLDER'] = 'static/school-maps/'
app.config['SESSION_COOKIE_SECURE'] = False


app.secret_key = env_to_var("FLASK_SECRET_KEY")
github_blueprint = make_github_blueprint(client_id=env_to_var("GITHUB_CLIENT_ID"),
                                         client_secret=env_to_var("GITHUB_CLIENT_SECRET"))

app.register_blueprint(github_blueprint, url_prefix="/login")

@app.route("/", methods=["GET", "POST"])
def index():
    
    try:
        if register_redirect:
            return redirect(url_for("register"))
    except:
        pass
    
    try:
        if login_redirect:
            return redirect(url_for("login"))
    except:
        pass
    
    if not github.authorized:
        return render_template("index.html")
    
    global resp
    resp = github.get("/user")
    
    assert resp.ok, resp.text

    school_info_needed = False
    
    mongo = MongoDBHandler()
    
    try:
        mongo.find_document("users", {"username": resp.json()['login']}['school'])
    except:
        school_info_needed = True
    finally:
        mongo.close_connection()
    
    return render_template("dashboard.html", username=resp.json()['login'], info=school_info_needed)

@app.route("/search_schools", methods=["GET"])
def search_schools():
    query = request.args.get('query', '')
    file_path = 'static/schools/Public_Schools.csv'
    column_name = 'NAME'
    results = search_csv_column(file_path, column_name, query)
    return jsonify(results)

@app.route("/login", methods=["GET", "POST"])
def login(): 
    resp_set()
    
    if request.method == "POST":
        cprint(f"User is a {request.form.get('role')}", "green", attrs=["bold"])
        mongo = MongoDBHandler()
        
        global login_redirect
        login_redirect = False
        
        try:
            resp.json()['login']
        except:
            login_redirect = True
            return redirect(url_for("github.login"))
        
        if mongo.find_document("users", {"username": resp.json()['login']}) != None:
            if mongo.find_document("users", {"username": resp.json()['login']})['role'] == request.form.get("role"):
                cprint("Roles match; redirecting to dashboard", "green", attrs=["bold"])
                return redirect(render_template("dashboard.html", username=resp.json()['login']))
            else:
                cprint("Roles dont match; throwing error", "green", attrs=["bold"])
                return render_template("error.html", message="User already exists with a different role.")
        else:
            mongo.insert_document("users", {"username": resp.json()['login'], "role": request.form.get("role")})
        mongo.close_connection()
        
        return redirect(render_template("dashboard.html", username=resp.json()['login']))
        
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    
    mongo = MongoDBHandler()
    
    version = False
    
    try:
        mongo.find_document("users", {"username": resp.json()['login']}['school'])
    except:
        version = True
    finally:
        mongo.close_connection()
        
    resp_set()
    
    global register_redirect
    register_redirect = False
    
    if not github.authorized:
        register_redirect = True
        
        return redirect(url_for("github.login"))
    
    if request.method == "POST":
        school_name = request.form.get('school_name')
        file = request.files['file']
        
        cprint(f"School Name: {school_name}", "green", attrs=["bold"])
        
        assert 'file' in request.files
        assert file.filename != ''

        if file:
            file.filename = f"{school_name}.png"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], school_name, file.filename)
            
            if os.path.exists(filepath):
                mongo = MongoDBHandler()
                if mongo.find_document("schools", {"school_name": school_name}) != None:
                    mongo.close_connection()
                else:
                    mongo.close_connection()
                    return render_template("error.html", message="File already exists. Please choose a different file name.")

            mongo = MongoDBHandler()
            mongo.insert_document("schools", {"school_name": school_name, "file": filepath})
            mongo.close_connection()
            
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)
            
            cprint("Dashboard", "green", attrs=["bold"])
            return render_template("dashboard.html", username=resp.json().get("login"))
    
    cprint("Register", "green", attrs=["bold"])
    return render_template("register.html", version=version)

def resp_set():
    global resp
    resp = github.get("/user")

if __name__ == "__main__":
    app.run(debug=True)