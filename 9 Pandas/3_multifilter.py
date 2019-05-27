# pip install pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# dataframe list of dictionary
data = [
    {'nama': 'Andi', 'nilai': 90},
    {'nama': 'Budi', 'nilai': 88},
    {'nama': 'Caca', 'nilai': 89},
    {'nama': 'Deni', 'nilai': 89},
    {'nama': 'Euis', 'nilai': 89}
]

dfData = pd.DataFrame(
    data, 
    index = list('abcde')
    )

print(dfData
    .iloc[0:5:2]
    .sort_values(
        by = ['nilai', 'nama'],
        ascending = [True, False]
    )[['nilai', 'nama']]
)
