import requests
import json

url = 'https://api.favoriot.com/v1/streams'
dataBody = {
    "device_developer_id": "deviceDefault@Lintang_Wisesa",
    "data": {
        "message": "Hello Favoriot!"
    }
}

headers = {
    'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkxpbnRhbmdfV2lzZXNhIiwicmVhZF93cml0ZSI6dHJ1ZSwiaWF0IjoxNDkzODgyODczfQ.0n_FIr4vapSjewJE2e7cb-FTXs3JsUMTHsTgT2mYNFs',
    "Content-Type": "application/json"
}

r = requests.post(url, data=json.dumps(dataBody), headers=headers)
print(r.content)