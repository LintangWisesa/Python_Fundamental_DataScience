
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3,4,5,6,7,8,9]
y = [0,4,9,3,5,8,4,10,5]

# plt.subplot2grid(figureShape(rows, cols), plotPosition(rows, cols))
# plotPosition: index starts from 0

plotA = plt.subplot2grid((2, 1), (0, 0))
plotA.plot(x, y)

plotB = plt.subplot2grid((2, 1), (1, 0))
plotB.scatter(x, y)

plt.show()

# ================================================================

# subplot2grid(figureShape(row,col), plotPosition(row,col))   
# NOTE: index position start from 0

# ax1 = plt.subplot2grid((1,1), (0,0))
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