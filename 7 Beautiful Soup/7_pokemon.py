# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

req = requests.get('https://pokemondb.net/pokedex/all')
soup = BeautifulSoup(req.content, 'html.parser')
# print(soup)

data = soup.find_all('td', class_='cell-num cell-fixed')
# print(len(data))
pokemon = []
for i in data:
    index = i.text
    pict = i.span.span['data-src']
    nama = i.find_next_sibling().a.string
    tipe = i.find_next_sibling().find_next_sibling().a.string
    x = {
        'index': index,
        'nama': nama,
        'tipe': tipe,
        'image': pict
    }
    pokemon.append(x)
print(pokemon)

import csv
with open('7_pokemon.csv', 'w', newline='', encoding='utf-8') as pokefile:
    kolom = ['index', 'nama', 'tipe', 'image']
    write = csv.DictWriter(pokefile, fieldnames=kolom)
    write.writeheader()
    write.writerows(pokemon)