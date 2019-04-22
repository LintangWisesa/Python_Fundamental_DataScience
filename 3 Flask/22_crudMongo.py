from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.EmployeeData

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data', methods=['POST', 'GET', 'DELETE', 'PUT'])
def data():

    # post data
    if request.method == 'POST':
        body = request.json
        id = body['id']
        name = body['name']
        age = body['age']
        country = body['country']
        
        # table name = Employees
        db.Employees.insert_one({
            "id": id,
            "name": name,
            "age": age,
            "country": country
        })
        return 'Anda sukses nge-POST!'

    # get all data, response as JSON
    elif request.method == 'GET':
        allData = db.Employees.find()
        dataJson = []
        for data in allData:
            id = data['id']
            name = data['name']
            age = data['age']
            country = data['country']
            dataDict = {
                'id': id,
                'name': name,
                'age': age,
                'country': country
            }
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)

    # delete id = 5
    elif request.method == 'DELETE':
        criteria = 5
        db.Employees.delete_many({"id":criteria})
        print('\nDeletion successful\n')
        return 'Successfully DELETE!'

    # edit data with 'id' from body request
    else:
        body = request.json
        criteria = body['id']
        name = body['name']
        age = body['age']
        country = body['country']

        db.Employees.update_one(
            {"id": criteria},
            {
                "$set": {
                    "name":name,
                    "age":age,
                    "country":country
                }
            }
        )
        print("\nRecords updated successfully\n")
        return 'Successfully PUT!'

if __name__ == '__main__':
    app.debug = True
    app.run()