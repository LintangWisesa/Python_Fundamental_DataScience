
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [2, 4, 6, 8, 10]
y = [4, 6, 8, 3, 9]
z = [1, 3, 5, 7, 9]

plt.bar(x, y, label='Diagram 1', color='r', yerr = 0.5) # red
plt.bar(x, z, label='Diagram 2', color='c', bottom=y, yerr = 0.5) # cyan
# grafik x-z ada di atas x-y

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend()

plt.show()