
import requests

nama = input('Ketik nama pemain : ')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p='+nama

data = requests.get(url)
output = data.json()

print(output)
# print(output['player'][0]['strNationality'])