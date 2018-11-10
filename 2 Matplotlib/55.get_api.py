
import matplotlib.pyplot as plt
import urllib

url = 'https://jsonplaceholder.typicode.com/users'
data = urllib.request.urlopen(url).read().decode()

print(data)