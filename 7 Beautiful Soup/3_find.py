### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup

### from html file:
soup = BeautifulSoup(open('0.html', 'r'), 'html.parser')

print(soup.find_all('p'))
print(soup.find_all('li'))
print(soup.find(id='tes'))

for nama in soup.find_all('li'):
    print(nama.string)