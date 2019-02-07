# default csv delimiter = ','

# https://www.programiz.com/python-programming/reading-csv-files
# https://www.programiz.com/python-programming/working-csv-files

import csv

with open('32a1.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    print(reader)
    for row in reader:
        print(row)

csvFile.close()