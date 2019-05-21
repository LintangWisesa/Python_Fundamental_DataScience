# ambil data power ranger, mulai siaran & akhir siaran

### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# lists of power rangers
r = requests.get("https://en.wikipedia.org/wiki/List_of_Power_Rangers_episodes")
soup = BeautifulSoup(r.content, 'html.parser')

dataPowerRanger = []

data = soup.find(class_='wikitable').tbody
for i in data.find_all('i'):
    if 'Ranger' in i.text:
        parent = i.find_parent()
        siblingPar = parent.find_next_siblings()
        dateStart = siblingPar[1].find('span', class_='bday dtstart published updated')
        dateEnd = siblingPar[2].find('span', class_='dtend')
        print(i.text, ' ✅ ', dateStart.text, ' ⛔ ', dateEnd.text)