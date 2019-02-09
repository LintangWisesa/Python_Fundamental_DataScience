
import matplotlib.pyplot as plt
import urllib
import json

url = 'https://jsonplaceholder.typicode.com/users'
data = urllib.request.urlopen(url).read().decode()
users = json.loads(data)

# print(data)
# print(users[1])
print(users[1].get('id'))
print(users[1].get('name'))