
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [5, 3, 6, 1, 7, 9, 3, 3, 2]

# plt.scatter(x, y, label='Tes', color='k', marker='*', s=200)
# plt.plot(x,y,'*')
# marker = '*' 'x' 'o' 'D' '$A$' baca docs

plt.scatter(
    x, y, s=300, marker='*',
    c = np.arange(0,1.2,0.1), cmap = 'hot_r', edgecolors = 'k'
)

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
# plt.legend()

plt.show()