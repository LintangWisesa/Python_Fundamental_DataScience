### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# lists of digimon
r = requests.get("https://wikimon.net/Visual_List_of_Digimon")
soup = BeautifulSoup(r.content, 'html.parser')

dataTarget = soup.find_all('table', class_='') # table yang tanpa class!
# print(len(dataTarget))        # 2-1280 data digimon dari 1281
# print(dataTarget[2:1280])
# print(dataTarget[2].tr.find_next_sibling())
# print(dataTarget[2].tr.find_next_sibling().a.text)

dataDigimon = []

for i in dataTarget[2:1280]:
        # print(i)
        nama = i.tr.find_next_sibling().a
        p = nama.find_parent()
        pp = p.find_parent()
        ppp = pp.find_parent()
        image = ppp.img['src']
        
        # print(nama.text)
        # print('https://wikimon.net'+image)

        data = {
                'nama': nama.text,
                'gambar': 'https://wikimon.net'+image
        }
        dataDigimon.append(data)

print(dataDigimon)

# save on csv
import csv

with open('{}.csv'.format('6_digimon'), 'w', newline = '', encoding="utf-8") as fileku:
        kolom = ['nama', 'gambar']
        tulis = csv.DictWriter(fileku, fieldnames = kolom)
        tulis.writeheader()
        tulis.writerows(dataDigimon)
