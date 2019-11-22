# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

req = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
soup = BeautifulSoup(req.content, 'html.parser')
strong = soup.find_all('strong')
data = []
for i in strong:
    data.append(i.text)
ultra = data[2:36]
monster = data[37:110]

print(ultra)
print(monster)