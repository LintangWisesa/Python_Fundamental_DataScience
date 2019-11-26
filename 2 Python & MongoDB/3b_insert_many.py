import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["py_mongo"]
mycol = mydb["users"]


mydata = [
    {'nama': 'Euis', 'usia': 35, 'kota': 'Denpasar'},
    {'nama': 'Fafa', 'usia': 29, 'kota': 'Jakarta'},
    {'nama': 'Gian', 'usia': 22, 'kota': 'Sorong'}
]
mycol.insert_many(mydata)