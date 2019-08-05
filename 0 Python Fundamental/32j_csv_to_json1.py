# ================================
# read csv
import csv

data = []

with open('32k_data.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        # print(dict(row))
        data.append(dict(row))

print(data)

# ================================
# import to json
import json

with open('32k_out.json', 'w') as f:
    json.dump(data, f)