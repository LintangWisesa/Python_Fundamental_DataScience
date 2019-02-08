import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]

# find data dg nama = 'Andi'
myquery = { "nama": "Andi" }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

# find data yg harga > 1000000
myquery = { "harga": {"$gt": 1000000} }
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)