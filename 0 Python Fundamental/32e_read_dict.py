# read as dictionary

import csv

csv.register_dialect('myDialect', delimiter = ',')

with open('32a1.csv', 'r') as csvFile:
    reader = csv.DictReader(csvFile, dialect='myDialect')
    for row in reader:
        print(dict(row))

csvFile.close()
