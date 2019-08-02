
import json

with open('31b_data.json') as f:
    data = json.load(f)
print(data)

with open('31c_data.json', 'w') as f:
    json.dump(data, f)