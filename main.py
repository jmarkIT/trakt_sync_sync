import requests
import json
import database
from client import client_id, access_token


api_url = "https://api.trakt.tv/"

get_shows_url = "sync/watched/shows"

get_progress_url = "https://api.trakt.tv/shows/legion/progress/watched"

headers = {
    "Content-type": "application/json",
    "trakt-api-key": client_id,
    "trakt-api-version": "2",
    "Authorization": "Bearer {}".format(access_token)
}


def get_shows(url, headers):
    r = requests.get(url, headers=headers)
    
    show_list = []
    shows = r.json()
    
    #print(shows)
    
    for show in shows:
    	if show["show"]["ids"]["slug"] not in show_list:
    		show_list.append(show["show"]["ids"]["slug"])
    
    
    return show_list	


def get_progress(url, headers):
    r = requests.get(url, headers=headers)
    show_progress = r.json()
    print(len(show_progress['seasons']))
    
    seasons = show_progress['seasons']
    
    for season in seasons:
    	season_number = season['number']
    	
    	episodes = season['episodes']
    	
    	print(episodes)

def full_update():
	#TODO: this function should call get_shows to get a list of shows, then use that list to pull relevant information
	# for each show using get_progress
	pass

if __name__ == '__main__':
    #show_progress_data = get_progress(get_progress_url, headers)
    
    show_sync_data = get_shows("https://api.trakt.tv/sync/watched/shows", headers)

    #print(show_progress_data)
    for title in show_sync_data:
    	print(title)
