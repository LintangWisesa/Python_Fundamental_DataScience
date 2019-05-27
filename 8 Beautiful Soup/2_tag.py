### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup

### from html file:
soup = BeautifulSoup(open('0.html', 'r'), 'html.parser')
print(soup.title)
print(soup.h1)
print(soup.p)

print(soup.h1)
print(soup.h1.name)
print(soup.h1.string)
print(soup.h1.text)

print(soup.get_text())