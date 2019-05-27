### web scraping: pip install beautifulsoup4
from bs4 import BeautifulSoup

### from html text:
soup = BeautifulSoup('<p>Some<b>bad<i>HTML', 'html.parser')
print(soup)

### from html file:
soup = BeautifulSoup(open('0.html', 'r'), 'html.parser')
print(soup)

### from website:
import requests
r = requests.get("https://ezalin.com")
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)

### from website using urllib
import urllib.request
url = urllib.request.urlopen('https://ezalin.com').read()
soup = BeautifulSoup(url, 'html.parser')
print(soup)