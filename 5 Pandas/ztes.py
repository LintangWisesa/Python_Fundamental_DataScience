# dataframe

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

y = np.random.randint(10, size=10)
data = {
    'satu': 'Hai',
    'dua': np.arange(10),
    'tiga': pd.Series(y),
    'empat': pd.Timestamp('20190220'),
    'lima': pd.date_range('20190220', periods = 10)
}

df = pd.DataFrame(data)
print(df)

plt.plot(df['lima'], df['tiga'])
plt.xticks(rotation=90)
plt.show()
