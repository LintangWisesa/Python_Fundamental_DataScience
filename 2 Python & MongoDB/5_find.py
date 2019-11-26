import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]

# print all data as list
print(list(mycol.find()))

# print every data
for x in mycol.find():
  print(x)

# ===========================================

nama = ['Andi', 'Euis', 'Fafa']
print(list(mycol.find({'nama': {'$in': nama}})))