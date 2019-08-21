
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

ages1 = [22, 23, 54, 60, 43, 31, 28, 21, 33, 39, 41, 56, 59, 26, 43, 54]
# ages2 = [18, 45, 32, 33, 21, 11, 45, 32, 44, 56, 50, 22, 24, 26, 19, 5]
bins = [0, 10, 20, 30, 40, 50, 60]  # range age

plt.hist(ages1, bins, histtype='stepfilled', rwidth=0.8)
# plt.hist([ages1, ages2], bins, histtype='bar', rwidth=0.8)
# histtype: bar, barstacked, step, stepfilled

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend(['Ages 1', 'Ages 2'])

plt.show()