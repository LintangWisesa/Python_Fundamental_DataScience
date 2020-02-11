import xlrd 
# pip install xlrd

loc = ("32z.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)                    # call by sheet index
# sheet = file.sheet_by_name('DataKaryawan')    # call by sheet name

print(sheet.nrows)
print(sheet.ncols)
print(sheet.cell_value(0, 0))   # row, col

for i in range(sheet.ncols): 
    print(sheet.cell_value(0, i))

for i in range(sheet.nrows): 
    print(sheet.cell_value(i, 0))

##########################################

data = []
for i in range(1,sheet.nrows):
    new = []
    for j in range(sheet.ncols):
        new.append(sheet.cell_value(i, j))
    data.append(tuple(new))
print(data)

##########################################

print(sheet.row_values(1))

for i in range(sheet.nrows): 
    print(sheet.row_values(i))
