
import json

with open('31b_data.json') as f:
    data = json.load(f)

print(data)


################################

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# y = json.dumps(x)   # convert python to json

# print(y)