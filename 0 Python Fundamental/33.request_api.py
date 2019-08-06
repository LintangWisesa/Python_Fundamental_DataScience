# pip install requests
# py -m pip install requests

import requests

url = 'https://jsonplaceholder.typicode.com/users/1'

data = requests.get(url)
output = data.json()

print(output)
# print(output['name'])
# print(output['address']['city'])