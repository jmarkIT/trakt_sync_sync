import requests
from client import client_id, access_token

url = "https://api.trakt.tv/users/dukkhalatte/watched/shows"

headers = {
    "Content-type": "application/json",
    "trakt-api-key": client_id,
    "trakt-api-version": "2",
    "Authorization": "Bearer {}".format(access_token)
}

def get_shows(url, headers):
    r = requests.get(url, headers=headers)
    print(r.status_code)
    print(client_id)
    print(r.content)

if __name__ == '__main__':
    get_shows(url, headers)