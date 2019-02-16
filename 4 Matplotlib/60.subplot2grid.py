
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3,4,5,6,7,8,9]
y = [0,4,9,3,5,8,4,10,5]

# subplot2grid(shape(row,col), loc(row,col))
ax1 = plt.subplot2grid((1,1), (0,0))
ax1 = plt.subplot2grid((2,2), (1,1))
ax1.plot(x,y)

# set garis spine / border
ax1.spines['left'].set_color('r')
ax1.spines['left'].set_linewidth(5)
ax1.spines['right'].set_color('b')
ax1.spines['right'].set_linewidth(5)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

# set label x / y
ax1.tick_params(axis='x', colors='y')
ax1.tick_params(axis='y', colors='g')
ax1.axhline(y[3], color='g', linewidth=5)
ax1.fill_between(x, y[3], 0, facecolor='g', alpha=0.3)
ax1.fill_between(x, y[8], y[3], facecolor='r', alpha=0.3)

plt.xlabel('Nilai x')
plt.ylabel('Nilai y')
plt.title('Tes Plotting Data')
plt.grid(True)
plt.legend(['Data'])
plt.show()