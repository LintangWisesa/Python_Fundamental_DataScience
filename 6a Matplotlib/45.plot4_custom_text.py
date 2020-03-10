
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd

x = [1,2,3,4,5,6,7,8,9]
y = [0,4,9,3,5,8,4,10,5]

plt.plot(x,y, 'ro')
plt.plot(x,y)

plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# custom text
plt.text(0, 0, 'titik\nawal')
plt.text(0,10,'titik maksimal')
plt.text(2,4,'tes',fontdict={'color':'red', 'family':'impact'})

for i in x:
    plt.text(i-.1, y[i-1]+.8, y[i-1])
    # show y val on (i-0.1 , y+0.8)

plt.grid(True)
plt.legend(['Data'], loc=4)
# plt.show()

# ===========================

x = np.array([1,2,3,4,5,6,7,8,9])

plt.plot(x, x**2, color='g', markerfacecolor='y',
    markeredgecolor = 'y', marker='o', linestyle='-', 
    markersize=6, linewidth = .1, label = 'My Data'
)
plt.grid(True)

for i in x**2:
    plt.text(x[list(x**2).index(i)]-.2, i+2, i)

# plt.show()

# =================================
x = [1,2,3,4,5,6,7,8,9]
y = [2,1,4,5,6,5,7,8,7]
df = pd.DataFrame({'X': x, 'Y': y})
plt.plot(df['X'], df['Y'], marker='o', mfc='red')

for i in df['X']:
    # plt.text(i-.1, df['Y'].iloc[i-1] + .3, df['Y'].iloc[i-1])
    plt.text(i-.1, df['Y'].iloc[i-1] + .3, '{},{}'.format(i, df['Y'].iloc[i-1]))
    # print(i)
    # print(df['Y'].iloc[i-1])

plt.show()