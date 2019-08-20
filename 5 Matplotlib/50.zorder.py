import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,1,2,3,4,5])
y = np.array([4,6,4,5,6,7])
z = np.array([2,3,2,3,2,2])

# tentukn urutan diagram, scatter di atas plot di atas bar
plt.scatter(x, y, label='Data 1', color='y',
    marker='*', s=250, zorder=3
)
plt.plot(x, y, 'r--', zorder=2)
plt.bar(x, y, color='lightblue', zorder=1)

plt.title('Diagram Batang')
plt.grid(True)
plt.legend()
plt.show()