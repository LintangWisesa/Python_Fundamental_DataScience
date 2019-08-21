# to zoom in/out: right click + drag mouse

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = plt.subplot(111, projection = '3d')

x = np.array([0,1,2,3,4,5,6,7,8,9])
y = np.array([0,1,2,3,4,5,6,7,8,9])
# z must be 2 dim
z = np.array([[0,1,2,3,4,5,6,7,8,9]])

ax.plot_wireframe(x, y, z, color='green', linestyle='--')
ax.set_xlabel('Nilai x')
ax.set_ylabel('Nilai y')
ax.set_zlabel('Nilai z')

plt.show()

# to zoom in/out: right click + drag mouse