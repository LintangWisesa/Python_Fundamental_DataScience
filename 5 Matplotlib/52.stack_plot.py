
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 1, 8, 2, 3, 5, 9, 1, 4]
z = [5, 6, 5, 7, 9, 1, 1, 6, 8, 8]
# x y z jumlah elemen harus sama

plt.stackplot(x, y, z, colors=['m','r','c'])

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# legend untuk stack, bisa dibuat dg plot kosong:
plt.plot([], [], color='m', label='x', linewidth=8)
plt.plot([], [], color='r', label='y', linewidth=8)
plt.plot([], [], color='c', label='z', linewidth=8)
plt.legend()

plt.show()