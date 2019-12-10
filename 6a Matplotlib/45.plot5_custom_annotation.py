
import matplotlib.pyplot as plt
# from matplotlib import pyplot as plt 

x = [1,2,3,4,5,6,7,8,9]
y = [0,4,9,3,5,8,4,10,5]

plt.plot(x,y,'g-o')

plt.title('Tes Plotting Data')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

plt.annotate('Nilai\ntertinggi', xy=(8, 10), xytext=(4.5, 9),
             arrowprops=dict(facecolor='black', shrink=0.1),
             # arrowprops = dict(arrowstyle = '<|-')
             )

plt.grid(True)
plt.legend(['Data'], loc=4)
plt.show()

# ==============================================================================
# docs: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.annotate.html

# plt.annotate(
#     'Highest value!', xy=(9, 729), xytext=(5,600),
#     arrowprops = {'facecolor':'red', 'arrowstyle':'-|>'}
# )

# if arrowprops contains arrowstyle, maka bbrp key forbidden: shrink, width, headwidth, headlength