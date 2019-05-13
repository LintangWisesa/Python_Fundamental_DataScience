
import matplotlib.pyplot as plt

slice = [9, 3, 5, 7]
activity = ['Tidur', 'Tahajud', 'Subuh', 'Berangkat']
# cols = ['c', 'm', 'r', 'k']

plt.pie(slice, labels=activity, autopct='%1.1f%%', textprops={'color':"r"})

# adding center circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Tes Plotting Data\nby Lintang Wisesa')
plt.show()