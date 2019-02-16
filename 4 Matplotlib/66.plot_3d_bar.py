import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = plt.subplot(111, projection = '3d')

x = [0,1,2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]
z = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = [0,1,2,3,4,5,6,7,8,9]

ax.bar3d(
    np.array(x), 
    np.array(y), 
    np.array(z),
    np.array(dx),
    np.array(dy),
    np.array(dz),
)

ax.set_xlabel('Nilai x')
ax.set_ylabel('Nilai y')
ax.set_zlabel('Nilai z')

plt.show()