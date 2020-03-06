# show frequences & relationships
import pandas as pd 

data = [
    {'nama':'Andi', 'sex':'L', 'usia': 21, 'kota':'Jakarta', 'status':'Belum Menikah'},
    {'nama':'Budi', 'sex':'P', 'usia': 22, 'kota':'Jakarta', 'status':'Menikah'},
    {'nama':'Caca', 'sex':'P', 'usia': 23, 'kota':'Jakarta', 'status':'Menikah'},
    {'nama':'Deni', 'sex':'L', 'usia': 24, 'kota':'Jakarta', 'status':'Belum Menikah'},
    {'nama':'Euis', 'sex':'L', 'usia': 25, 'kota':'Jakarta', 'status':'Belum Menikah'},
    {'nama':'Fafa', 'sex':'P', 'usia': 26, 'kota':'Bandung', 'status':'Menikah'},
    {'nama':'Gaga', 'sex':'L', 'usia': 27, 'kota':'Bandung', 'status':'Menikah'},
    {'nama':'Hani', 'sex':'P', 'usia': 28, 'kota':'Bandung', 'status':'Belum Menikah'},
    {'nama':'Inka', 'sex':'L', 'usia': 29, 'kota':'Bandung', 'status':'Menikah'},
    {'nama':'Jeni', 'sex':'P', 'usia': 30, 'kota':'Bandung', 'status':'Belum Menikah'}
]

df = pd.DataFrame(data)

print(pd.crosstab(df.kota, df.status))
# print(pd.crosstab(df['kota'], df['status']))

# print(pd.crosstab(df.sex, df.status, margins=True))
# print(pd.crosstab(df.sex, [df.status, df.kota], margins=True))

# show rata-rata jumlah yg single/married
# print(pd.crosstab(df.sex, df.status, normalize='index'))

# show rata-rata usia yg single/married
print(pd.crosstab(df.sex, df.status, values=df.usia, aggfunc='mean'))