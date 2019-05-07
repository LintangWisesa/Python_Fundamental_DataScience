# pip install pymongo
# py -m pip install pymongo

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# OR:

# from pymongo import MongoClient
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# get all db name = show dbs
print(myclient.list_database_names())