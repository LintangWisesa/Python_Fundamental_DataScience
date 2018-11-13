
import matplotlib.pyplot as plt
from matplotlib import style

# style.use('ggplot')
# style.use('fivethirtyeight')
style.use('dark_background')

print(plt.style.available)
print(plt.__file__) 
# untuk edit style, go to C:\Python37\Lib\site-packages\matplotlib\mpl-data\stylelib lalu edit codenya!

x = [1,2,3,4,5,6,7,8,9]
y = [0,4,9,3,5,8,4,10,5]
z = [3,5,6,1,2,9,8,7,3]

ax1 = plt.subplot2grid((1,1), (0,0))
ax1.plot(x,y)
ax1.plot(x,z)

plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.title('Tes Plotting Data')
plt.grid(True)
plt.legend(['Data'])
plt.show()