
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3,4,5,6,7,8,9]
y = [0,4,9,3,5,8,4,10,5]

plt.plot(x,y, 'ro')
plt.plot(x,y)

plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# custom text
plt.text(0, 0, 'titik\nawal')
plt.text(0,10,'titik maksimal')
for i in x:
    plt.text(i-.1, y[i-1]+.8, y[i-1])
    # show y val on (i-0.1 , y+0.8)

plt.grid(True)
plt.legend(['Data'], loc=4)
plt.show()