import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]

mydata = { "nama": "Budi", "usia": "26" }
x = mycol.insert_one(mydata)

# get id dari data yg baru saja terkirim
print(x.inserted_id)