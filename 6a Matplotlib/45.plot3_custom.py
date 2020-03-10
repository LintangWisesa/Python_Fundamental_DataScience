
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd

x = [1,2,3,4,5,6,7,8,9]
y = [0,4,9,3,5,8,4,10,5]

plt.plot(x,y)

plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.fill_between(x, y)
# plt.fill_between(x, y, 0, facecolor='g', alpha=0.3)
# plt.fill_between(x, y, 5, alpha=0.3)
# plt.fill_between(x, y[3], 0, facecolor='g', alpha=0.3)        # y[3] = batas bawahnya y elemen ke-3
# plt.fill_between(x, y[8], y[3], facecolor='r', alpha=0.3)     # y[8] = batas bawahnya y elemen ke-8

plt.grid(True)
plt.legend(['Data'])
plt.show()

# ==================================
# fill betweenx
x = [1,2,3,4,5,6,7,8,9]
y = [2,1,4,5,6,5,7,8,7]
df = pd.DataFrame({'X': x, 'Y': y})

plt.plot(df['X'], df['Y'])
plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.9)
plt.fill_between(df['X'], 5, 3, facecolor='y', alpha=0.3)
plt.fill_betweenx([0,8], 5, 3, facecolor='g', alpha=0.3)
plt.show()