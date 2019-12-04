import pandas as pd
import numpy as np 

# jika diperlukan: pip install html5lib
# file html harus mengandung <table>!
df = pd.read_html('8.html')
print(df)
print(df[0])
print(type(df[0]))

# ====================================
# read from http url
df = pd.read_html('http://digidb.io/digimon-list/')
print(df[0])

# ====================================
# read from https url using requests
import requests
url = 'https://pokemondb.net/pokedex/all'
x = requests.get(url)
df = pd.read_html(x.text)
print(df[0])