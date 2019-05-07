import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]

mydata = { "nama": "Andi", "usia": "27" }
x = mycol.insert_one(mydata)