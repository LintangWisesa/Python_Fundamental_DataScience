import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import csv

fig = plt.figure()
ax = plt.subplot(111, projection = '3d')

prov = []
dz1 = []
dz2 = []
with open('54_datarokok.csv', 'r') as fileku:
    reader = csv.reader(fileku)
    for x in reader:
        data = [x[0], float(x[1]), float(x[2])]
        prov.append(x[0])
        dz1.append(float(x[1]))
        dz2.append(float(x[2]))

print(prov)
print(dz1)
print(dz2)

prov.remove(prov[0])
dz1.remove(dz1[0])
dz2.remove(dz2[0])

x1 = np.arange(len(dz1))
y1 = np.zeros(len(dz1))
z1 = np.zeros(len(dz1))
dx1 = np.repeat(.1, len(dz1))
dy1 = np.repeat(.25, len(dz1))
# print(x1)
# print(y1)
# print(z1)
# print(dx1)
# print(dy1)

x2 = np.arange(len(dz2))
y2 = np.repeat(.6, len(dz2))
z2 = np.zeros(len(dz2))
dx2 = np.repeat(.1, len(dz2))
dy2 = np.repeat(.25, len(dz2))

ax.bar3d(
    np.array(x1), 
    np.array(y1), 
    np.array(z1),
    np.array(dx1),
    np.array(dy1),
    np.array(dz1),
    color = 'red',
)

ax.bar3d(
    np.array(x2), 
    np.array(y2), 
    np.array(z2),
    np.array(dx2),
    np.array(dy2),
    np.array(dz2),
    color = 'yellow',
)

ax.set_xlim(0, len(dz1))
ax.set_ylim(0, 1)

# ax.set_xlabel('Nilai x')
# ax.set_ylabel('Nilai y')
# ax.set_zlabel('Nilai z')

plt.yticks([.14, .74], [2015, 2016])
plt.xticks(x1, prov)
plt.xticks(rotation = 90)
plt.show()