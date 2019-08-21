import matplotlib.pyplot as plt
fig,ax = plt.subplots()
ax.plot([1,2,3],[10,-10,30])

import pickle
pickle.dump(fig, open('66save3d.fig.pickle', 'wb')) 
