
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)   # convert json to python dictionary

print(y)
print(y["age"])

################################

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)   # convert python to json

print(y)