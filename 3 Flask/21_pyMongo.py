# install pymongo: $ pip install pymongo

from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.EmployeeData
# database name = EmployeeData

# Function to insert data into mongo db
def insert():
    employeeId = input('Enter Employee id :')
    employeeName = input('Enter Name :')
    employeeAge = input('Enter age :')
    employeeCountry = input('Enter Country :')
    # table name = Employees
    db.Employees.insert_one({
        "id": employeeId,
        "name":employeeName,
        "age":employeeAge,
        "country":employeeCountry
    })
    print('\nInserted data successfully\n')

# function to read records from mongo db
def read():
    empCol = db.Employees.find()
    print('\n All data from EmployeeData Database \n')
    for emp in empCol:
        print(emp)

# Function to update record to mongo db
def update():
    criteria = input('\nEnter id to update\n')
    name = input('\nEnter name to update\n')
    age = input('\nEnter age to update\n')
    country = input('\nEnter country to update\n')

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

# Function to delete record from mongo db
def delete():
    criteria = input('\nEnter employee id to delete\n')
    db.Employees.delete_many({"id":criteria})
    print('\nDeletion successful\n') 

# insert()
# read()
# update()
delete()