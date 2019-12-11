import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'x': [1,2,3,4,5],
    'y': [9,5,7,3,6],
    'z': [2,3,4,5,3]
})

plt.figure(1)
plt.bar(df.x, df.y, 
    color='pink', edgecolor='black', linewidth=5,
)
# y val bar
for i in df['y']:
    plt.text(
        df[df['y'] == i]['x']-.1, i+.2, i,
        fontdict={'size':20}
    )

plt.figure(2)
plt.barh(df.x, df.y)
# y val barh
for i in df['y']:
    plt.text(
        i+.2, df[df['y'] == i]['x']-.1, i,
        fontdict={'size':20}
    )

plt.show()