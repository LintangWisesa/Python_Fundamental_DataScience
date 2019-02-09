
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3]
y = [1,4,9]
z = [10, 5, 0]

plt.plot(x,y,'o')
plt.plot(x,z,'*')
# marker 'o' '*'

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y dan z')
plt.legend(['Garis x-y', 'Garis x-z'])

plt.show()

# plt.plot(x, y, color='m', label='Tes', linewidth=5)
# plt.legend()