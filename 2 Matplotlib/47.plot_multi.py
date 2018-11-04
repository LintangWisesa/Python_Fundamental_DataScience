
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3]
y = [1,4,9]
z = [10, 5, 0]

plt.plot(x,y)
plt.plot(x,z)

plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y dan z')
plt.legend(['Ini y', 'Ini z'])

plt.show()