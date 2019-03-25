import pandas as pd 

dataSuhu = [
    {'hari':'Senin', 'Jakarta':34, 'Bandung':21},
    {'hari':'Selasa', 'Jakarta':39, 'Bandung':22},
    {'hari':'Rabu', 'Jakarta':35, 'Bandung':20},
    {'hari':'Kamis', 'Jakarta':34, 'Bandung':22},
    {'hari':'Jum\'at', 'Jakarta':38, 'Bandung':21},
    {'hari':'Sabtu', 'Jakarta':36, 'Bandung':20},
    {'hari':'Ahad', 'Jakarta':38, 'Bandung':19}
]

df = pd.DataFrame(dataSuhu)

# basic melt
# df1 = pd.melt(df, id_vars=['hari'])
# print(df1)
# print(df1[df1['kota'] == 'Bandung'])

# custom melt with var & val name
df1 = pd.melt(df, id_vars=['hari'], var_name='kota', value_name='suhu')
print(df1)
print(df1[df1['kota'] == 'Bandung'])