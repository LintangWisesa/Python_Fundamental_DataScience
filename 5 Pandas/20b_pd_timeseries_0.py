
# historical price & data / data historis saham 
# https://www.nasdaq.com/symbol/aapl/historical
# https://finance.yahoo.com/quote/AALI.JK/history?ltr=1
# https://www.seputarforex.com/saham/data_historis/

# =============================================

# panduan olah data saham
# http://rudiyanto.blog.kontan.co.id/2017/05/02/panduan-mencari-dan-mengolah-data-return-saham-bagian-1/comment-page-3/

# =============================================

import pandas as pd

# df = pd.read_csv('20_Apple_Stock_Price.csv)
# print(df)

# cek tipe data kolom 'date'
# print(type(df.date[0]))
# print(type(df['date'][0]))
# ternyata 'str' bukan date! untuk merubahnya jadi 'date':

# ========================================

# df = pd.read_csv('20_Apple_Saham.csv', parse_dates=['date'])
# print(df)
# print(type(df['date'][0]))

# ========================================

# ubah kolom 'date' sbg index dataframe:
df = pd.read_csv(
    '20_Apple_StockPrice.csv', 
    parse_dates=['date'], 
    index_col='date'
)

# print(df)

# show data pada bulan Februari 2019
# print(df['2019-02'])
print(df['2019-02-01'])
print(df['01-02-2019'])
# print(df['2019-02-07' : '2019-02-01'])
# print(df['01-29-2019' : '02-11-2019'])

# show rata2 nilai close pada Feb 2019
# print(df['2019-02']['close'].mean())
# print(df['2019-02'].close.mean())
# print(df['2019-02']['close'].max())
# print(df['2019-02']['close'].min())