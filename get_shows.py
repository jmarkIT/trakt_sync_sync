import requests
from client import client_id

url = "https://api.trakt.tv/shows/dukkhalatte/progress/watched"

headers = {
    "Content-type": "application/json",
    "trakt-api-key": client_id,
    "trakt-api-version": "2"
}

r = requests.get(url, headers=headers)

print(r.status_code)

print(client_id)