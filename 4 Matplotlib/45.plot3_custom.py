
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3,4,5,6,7,8,9]
y = [0,4,9,3,5,8,4,10,5]

plt.plot(x,y)

plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.fill_between(x, y, 0)
# plt.fill_between(x, y, 0, facecolor='g', alpha=0.3)
# plt.fill_between(x, y, 5, alpha=0.3)
# plt.fill_between(x, y[3], 0, facecolor='g', alpha=0.3)
# plt.fill_between(x, y[8], y[3], facecolor='r', alpha=0.3)

plt.grid(True)
plt.legend(['Data'])
plt.show()