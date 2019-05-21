### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# lists of pokemon
r = requests.get("https://pokemondb.net/pokedex/national")
soup = BeautifulSoup(r.content, 'html.parser')

data = soup.find_all('div', class_='infocard')
for i in data:
        no = i.find('small')
        nama = i.find('a', class_='ent-name')
        print(no.text, nama.text)