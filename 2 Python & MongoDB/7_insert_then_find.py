import pymongo

url = 'mongodb://localhost:27017'
mydb = pymongo.MongoClient(url)

newdb = mydb["gudang"]
newcol = newdb["produk"]
newdata = {"nama": "Celana", "harga": 5000000}
add = newcol.insert_one(newdata)
newid = add.inserted_id

for data in newcol.find({'_id': newid}):
    print('Data sukses terkirim!')
    print(data)