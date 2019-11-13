
import json

with open('31b_data.json', 'r') as f:
    data = json.load(f)

# print(data)

# =======================

with open('31b_data2.json', 'r') as f:
    data = json.load(f)
# print(data)

kolom = list(data[0].keys())
out = []
for i in data:
    out.append(list(i.values()))
print(kolom)
print(out)