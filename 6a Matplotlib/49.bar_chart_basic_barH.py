
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [2, 4, 6, 8, 10]
y = [4, 6, 8, 3, 9]
z = [1, 3, 5, 7, 9]

plt.barh(x, y, label='Diagram 1', color='r') # red
plt.barh(x, z, label='Diagram 2', color='c') # cyan
# plt.barh(x, y, label='Data 1', 
#     color=['r', 'g', 'b', 'k', 'y', 'r']
# )
# plt.barh(x, y, 
#     color=['r', 'g', 'b', 'y', 'k'], 
#     edgecolor='black', linewidth=5, height=0.3
# )

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.legend()

plt.show()