from py_tools import *

mongo = MongoDBHandler()

mongo.print_all_documents()

mongo.close_connection()