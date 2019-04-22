import csv
import matplotlib.pyplot as plt 
import numpy as np 

prov = []
rokok15 = []
rokok16 = []
with open('54_datarokok.csv', 'r') as fileku:
    reader = csv.reader(fileku)
    for x in reader:
        prov.append(x[0])
        rokok15.append(float(x[1]))
        rokok16.append(float(x[2]))

prov.remove(prov[0])
rokok15.remove(rokok15[0])
rokok16.remove(rokok16[0])

rokok15 = np.array(rokok15)
rokok16 = np.array(rokok16)
print(prov)
print(rokok15)
print(rokok16)

plt.bar(prov, rokok15)
plt.show()