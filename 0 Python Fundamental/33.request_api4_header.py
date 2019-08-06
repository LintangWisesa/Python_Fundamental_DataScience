
import requests

# cari kebab di jakarta via zomato api
url = 'https://developers.zomato.com/api/v2.1/search?entity_id=74&entity_type=city&q=kebab'
apikey = 'd1b8cea4661437f143641aabd01544f7'
headers = {
    'user-key': apikey
}

data = requests.get(url, headers=headers)
daftarMakanan = data.json()
print(daftarMakanan)

