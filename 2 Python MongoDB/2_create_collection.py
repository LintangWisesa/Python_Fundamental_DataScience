import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]

print(myclient.list_database_names())