
# custom delimiter

import csv

with open('32a2.csv', 'r') as csvFile:
    reader = csv.reader(csvFile, delimiter='|')
    for row in reader:
        print(row)

csvFile.close()