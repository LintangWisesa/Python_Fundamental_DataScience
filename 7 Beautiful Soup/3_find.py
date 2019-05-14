### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup

### from html file:
soup = BeautifulSoup(open('0.html', 'r'), 'html.parser')

print(soup.find_all('p'))
print(soup.find_all('li'))

print(soup.find(id='tes'))
print(soup.find(class_='halo'))
print(soup.find(class_='halo').text)

# # show all text inside <li>
# for nama in soup.find_all('li'):
#     print(nama.string)

# # show all <li> text inside <ol> only
# ol = soup.ol
# for barang in ol.find_all('li'):
#     print(barang.text)