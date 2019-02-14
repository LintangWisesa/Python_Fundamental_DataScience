import csv
import matplotlib.pyplot as plt 
import numpy as np 

allData = []
prov = []
rokok15 = []
rokok16 = []

with open('54_datarokok.csv', 'r') as fileku:
    reader = csv.reader(fileku)
    for x in reader:
        data = [x[0], float(x[1]), float(x[2])]
        allData.append(data)
        prov.append(x[0])
        rokok15.append(float(x[1]))
        rokok16.append(float(x[2]))

allData.remove(allData[0])
prov.remove(prov[0])
rokok15.remove(rokok15[0])
rokok16.remove(rokok16[0])
# print(allData)
# print(prov)
# print(rokok15)
# print(rokok16)

ratarokok15 = np.mean(rokok15)
ratarokok16 = np.mean(rokok16)
# print(ratarokok15)
# print(ratarokok16)

overrokok = []
for x in allData:
    if x[1] > ratarokok15 and x[2] > ratarokok16:
        overrokok.append(x)

provover = []
rokok15over = []
rokok16over = []
for x in overrokok:
    provover.append(x[0])
    rokok15over.append(x[1])
    rokok16over.append(x[2])

rokok15 = np.array(rokok15)
rokok16 = np.array(rokok16)
rata15 = np.repeat(ratarokok15, len(provover))
rata16 = np.repeat(ratarokok16, len(provover))

plt.bar(provover, rokok15over, color='yellow')
plt.bar(provover, rokok16over, color='lightblue')
plt.plot(provover, rata15, 'g-', linewidth=3)
plt.plot(provover, rata16, 'r-', linewidth=3)
plt.xticks(rotation=90)
plt.legend(['2015', '2016'], loc=3)
plt.show()