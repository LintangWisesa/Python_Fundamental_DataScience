
import requests

nama = input('Ketik klub bola : ')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+nama

data = requests.get(url)
listpemain = data.json()['player']

for name in listpemain:
    if name['strPosition'] == 'Goalkeeper':
        print(name['strPlayer'])

