import xlrd 
loc = ("32z.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)                    # call by sheet index
# sheet = file.sheet_by_name('DataKaryawan')    # call by sheet name

data = []
for i in range(sheet.nrows): 
    data.append(sheet.row_values(i))
# print(data)

out = []
for i in data:
    out.append(dict(zip(data[0], i)))
out = out[1:]
print(out)

# ========================================

import json
with open('32z.json', 'w') as f:
    json.dump(out, f)