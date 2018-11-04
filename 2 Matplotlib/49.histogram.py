
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

ages = [22, 23, 54, 60, 43, 31, 28, 21, 33, 39, 41, 56, 59, 26, 43, 54]
bins = [0, 10, 20, 30, 40, 50, 60]

plt.hist(ages, bins, histtype='bar', rwidth=0.8)

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
# plt.legend()

plt.show()