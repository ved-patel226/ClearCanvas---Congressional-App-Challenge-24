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
    if not github.authorized:
        return render_template("index.html")
    
    resp = github.get("/user")
    assert resp.ok, resp.text
    
    return render_template("index.html")

@app.route("/search_schools", methods=["GET"])
def search_schools():
    query = request.args.get('query', '')
    file_path = 'static/schools/Public_Schools.csv'
    column_name = 'NAME'
    results = search_csv_column(file_path, column_name, query)
    return jsonify(results)

@app.route("/register", methods=["GET", "POST"])
def register():
    if not github.authorized:
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
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)
    
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)