### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

### from html file:
r = requests.get("https://www.tokopedia.com/search?st=product&q=drone")
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())