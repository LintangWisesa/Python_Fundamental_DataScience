
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = [
    {'kota': 'Jakarta', 'suhu': 34, 'angin': 55},
    {'kota': 'Jakarta', 'suhu': 31, 'angin': 35},
    {'kota': 'Jakarta', 'suhu': 29, 'angin': 25},
    {'kota': 'Bandung', 'suhu': 18, 'angin': 85},
    {'kota': 'Bandung', 'suhu': 22, 'angin': 75},
    {'kota': 'Bandung', 'suhu': 20, 'angin': 85},
    {'kota': 'Surabaya', 'suhu': 34, 'angin': 65},
    {'kota': 'Surabaya', 'suhu': 38, 'angin': 75},
    {'kota': 'Denpasar', 'suhu': 29, 'angin': 85},
    {'kota': 'Denpasar', 'suhu': 21, 'angin': 25},
]
df = pd.DataFrame(data)

# group dataframe by 'kota'
g = df.groupby('kota')

# show data for Jakarta
print(g.get_group('Jakarta'))

# show max val for each data in each kota
print(g.max())
print(g.min())
print(g.mean())
