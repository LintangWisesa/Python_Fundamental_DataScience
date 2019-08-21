# read
import pickle
figx = pickle.load(open('66save3d.fig.pickle', 'rb'))

figx.show()

# get data from 3d plot
data = figx.axes[0].lines[0].get_data()
print(data)