# delimiter ',' with space

import csv

csv.register_dialect('myDialect', delimiter = ',', skipinitialspace=True)

with open('32a2.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, dialect='myDialect')
    for row in reader:
        print(row)

csvFile.close()