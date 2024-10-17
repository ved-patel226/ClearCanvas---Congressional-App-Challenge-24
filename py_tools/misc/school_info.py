from py_tools import MongoDBHandler
from termcolor import cprint


def get_school_info(resp):
    mongo = MongoDBHandler()

    try:
        mongo.find_document("users", {"username": resp.json()['login']})['school']
    except:
        school_info_needed = 0
        school_info = None
    else:
        if mongo.find_document("users", {"username": resp.json()['login']})['school'] == None:
            school_info_needed = 0
            school_info = None
        else:
            school_info_needed = 1
            school = mongo.find_document("users", {"username": resp.json()['login']})['school']
            cprint(f"School: {school}", "grey", attrs=["bold"])
            
            school_info = mongo.find_document("schools", {"school_name": school})
            
            cprint(school_info, "grey", attrs=["bold"])
            
    return school_info_needed, school_info