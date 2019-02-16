import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = [0,1,2,3,4,5,6,7,8,9]
y = [0,1,2,3,4,5,6,7,8,9]
z = [[0,1,2,3,4,5,6,7,8,9]]

ax.plot_wireframe(np.array(x), np.array(y), np.array(z))
ax.set_xlabel('Nilai x')
ax.set_ylabel('Nilai y')
ax.set_zlabel('Nilai z')

plt.show()