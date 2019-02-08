import pymongo

url = 'mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)

newdb = mydb["gudang"]
newcol = newdb["produk"]

data = {'$and': [
    {'harga': {'$gt': 300000}}, 
    {'harga': {'$lt': 3000000}}
]}
newdata = {"$set": {"kota": "Bogor"}}
newcol.update_many(data, newdata)

for x in newcol.find():
    print(x)