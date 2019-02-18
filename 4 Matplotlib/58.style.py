
import matplotlib.pyplot as plt

plt.style.use('dark_background')
# ['seaborn-dark', 'dark_background', 'seaborn-pastel', 
# 'seaborn-colorblind', 'tableau-colorblind10', 'seaborn-notebook', 
# 'seaborn-dark-palette', 'grayscale', 'seaborn-poster', 
# 'seaborn', 'bmh', 'seaborn-talk', 'seaborn-ticks', 
# '_classic_test', 'ggplot', 'seaborn-white', 'classic', 
# 'Solarize_Light2', 'seaborn-paper', 'fast', 
# 'fivethirtyeight', 'seaborn-muted', 'seaborn-whitegrid', 
# 'seaborn-darkgrid', 'seaborn-bright', 'seaborn-deep']

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