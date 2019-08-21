### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup

### from html file:
soup = BeautifulSoup(open('0.html', 'r'), 'html.parser')
print(soup.prettify())