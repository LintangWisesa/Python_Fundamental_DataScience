import pymongo

url = 'mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)

newdb = mydb["gudang"]
newcol = newdb["produk"]

data = {}
newdata = {"$set": {"kota": "Jakarta"}}
newcol.update_many(data, newdata)

for x in newcol.find():
    print(x)