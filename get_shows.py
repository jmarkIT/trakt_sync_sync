import requests
import json
import yaml

with open('secrets.yaml', 'r') as stream:
    data = yaml.safe_load(stream)
    client_id = data['client_id']
    client_secret = data['client_secret']
    access_token = data['token']['access']

api_url = "https://api.trakt.tv/"

get_shows_url = "sync/watched/shows"

get_progress_url = "https://api.trakt.tv/shows/game-of-thrones/progress/watched"

headers = {
    "Content-type": "application/json",
    "trakt-api-key": client_id,
    "trakt-api-version": "2",
    "Authorization": "Bearer {}".format(access_token)
}


def get_shows(url, headers):
    r = requests.get(url, headers=headers)
    return r.content


def get_progress(url, headers):
    r = requests.get(url, headers=headers)
    return r.json()


if __name__ == '__main__':
    show_progress_data = get_progress(get_progress_url, headers)

    print(show_progress_data)
