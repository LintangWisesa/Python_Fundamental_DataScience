import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]

# delete data dg nama = 'Andi'
myquery = { "nama": "Andi" }
mycol.delete_one(myquery)