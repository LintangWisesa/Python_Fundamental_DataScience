import requests

host = 'https://developers.zomato.com/api/v2.1'
cari = input('Kamu mau makan apa? : ')
url = f'{host}/search?entity_id=74&q={cari}'
apikey = 'd1b8cea4661437f143641aabd01544f7'
headers = {
    'user-key': apikey,
    'Content-Type': 'application/json'
}

data = requests.get(url, headers=headers)
listResto = data.json()['restaurants']
for i in listResto:
    print(
        '⭐ ', i['restaurant']['name'], ':', 
        i['restaurant']['location']['address']
    )
# print(len(listResto))
