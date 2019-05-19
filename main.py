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

def create_progress_url(slug):
    return f"https://api.trakt.tv/shows/{slug}/progress/watched"

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
    
    episode_info = []
    
    for season in seasons:
    	season_number = season['number']
    	
    	episodes = season['episodes']
    	
    	for episode in episodes:
    		print(episode)

def full_update():
	#TODO: this function should call get_shows to get a list of shows, then use that list to pull relevant information
	# for each show using get_progress
    #conn = database.create_connection("trakt_shows.db")

    all_shows = get_shows(api_url + get_shows_url, headers)

    for show in all_shows:
        url = create_progress_url(show)
        

    return None
    

if __name__ == '__main__':
    #show_progress_data = get_progress(create_progress_url("game-of-thrones"), headers)
    
    #show_sync_data = get_shows("https://api.trakt.tv/sync/watched/shows", headers)
    full_update()