import requests
from client import client_id

url = "https://api.trakt.tv/oauth/device/code"

headers = {
    "Content-type": "application/json"
}

parameters = {
    "client_id": client_id
}

r = requests.get(url, headers=headers, params=parameters)

print(r.status_code)