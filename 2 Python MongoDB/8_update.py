import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]

myquery = { "nama": "Budi" }
newvalues = { "$set": { "nama": "Bambang" } }
mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)