
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = [
    {'kota': 'Bandung', 'provinsi':'Jawa Barat', 'suhu': 34, 'angin': 55},
    {'kota': 'Bandung', 'provinsi':'Jawa Barat', 'suhu': 31, 'angin': 35},
    {'kota': 'Bandung', 'provinsi':'Jawa Barat', 'suhu': 29, 'angin': 25},
    {'kota': 'Cimahi', 'provinsi':'Jawa Barat', 'suhu': 18, 'angin': 85},
    {'kota': 'Cimahi', 'provinsi':'Jawa Barat', 'suhu': 22, 'angin': 75},
    {'kota': 'Surabaya', 'provinsi':'Jawa Timur', 'suhu': 20, 'angin': 85},
    {'kota': 'Surabaya', 'provinsi':'Jawa Timur', 'suhu': 34, 'angin': 65},
    {'kota': 'Surabaya', 'provinsi':'Jawa Timur', 'suhu': 38, 'angin': 75},
    {'kota': 'Malang', 'provinsi':'Jawa Timur', 'suhu': 29, 'angin': 85},
    {'kota': 'Malang', 'provinsi':'Jawa Timur', 'suhu': 21, 'angin': 25},
]
df = pd.DataFrame(data)

# ============================================
# group dataframe by 'provinsi' & 'kota'
g = df.groupby(['provinsi', 'kota'])

# print(g.groups.keys())
# print(g.first())

print(g.get_group(('Jawa Barat', 'Bandung')))