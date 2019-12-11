
# pip install matplotlib
# py -m pip install matplotlib

import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3,4,5,6,7,8,9]
y = [1,4,9,3,5,8,4,2,5]

plt.plot(x,y)

plt.title('Tes Plotting Data', fontdict={'fontsize': 20})
# plt.title('Ini bar chart', fontdict={
#     'family':'impact', 'size': 30, 'color':'lightgreen'
# })

plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.grid(True)
plt.legend(['Dataku'])
plt.show()