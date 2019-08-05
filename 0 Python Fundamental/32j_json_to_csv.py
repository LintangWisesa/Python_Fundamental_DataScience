# ================================
# read json
import json

with open('32k_data.json', 'r') as f:
    data = json.load(f)

print(data)

# ================================
# import to csv
import csv

with open('32k_out.csv', 'w', newline = '') as fileku:
    # kolom = ['nama', 'usia', 'kota']
    kolom = list(data[0].keys())
    tulis = csv.DictWriter(fileku, fieldnames = kolom)
    tulis.writeheader()
    tulis.writerows(data)