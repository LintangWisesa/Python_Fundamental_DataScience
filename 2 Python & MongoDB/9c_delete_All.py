import pymongo

url = 'mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)

newdb = mydb["gudang"]
newcol = newdb["produk"]

data = {}
newcol.delete_many(data)

for x in newcol.find(data):
    print(x)