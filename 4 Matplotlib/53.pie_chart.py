
import matplotlib.pyplot as plt

slice = [9, 3, 5, 7]
activity = ['Tidur', 'Tahajud', 'Subuh', 'Berangkat']
# cols = ['c', 'm', 'r', 'k']

plt.pie(slice, labels=activity)
# plt.pie(slice, labels=activity, colors=cols)
# plt.pie(slice, labels=activity, startangle=90)
# plt.pie(slice, labels=activity, shadow=True)
# plt.pie(slice, labels=activity, explode=(0,0.2,0,0))
# plt.pie(slice, labels=activity, autopct='%1.1f%%')

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.show()