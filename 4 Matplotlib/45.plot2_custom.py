
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3,4,5,6,7,8,9]
y = [1,4,9,3,5,8,4,2,5]

plt.plot(x,y)
# plt.plot(x, y, '-', label='Data', color='g', linewidth=5)
# plt.plot(x, y, '--', label='Data')
# plt.plot(x, y, '.', label='Data')
# plt.plot(x, y, '*', label='Data')

plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.90, wspace=0.2, hspace=0.2)
plt.grid(True)
# plt.grid(True, color='g', linestyle='-', linewidth=5)
# plt.grid(True, color='g', linestyle='--')

plt.legend()
plt.show()