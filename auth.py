import requests
import json
import time
from client import client_id, client_secret


url = 'https://api.trakt.tv/oauth/device/code'

headers = {
    'Content-Type': 'applications/json'
}

def device_code():
    # This function POSTs to the trakt.tv api to get a code
    # for OAuth setup
    # Returns a device code
    
    params = {
    "client_id": client_id
    }

    r = requests.post(url, params=params, headers=headers)

    output= json.loads(r.content)
    device_code = output["device_code"]
    user_code = output["user_code"]
    verification_url = output["verification_url"]
    print("Your usercode is {}, please go to {} to activate".format(user_code, verification_url))

    return device_code


def get_token(code):
	# Takes a device code and uses it to get access and
	# refresh tokens for the users account
	
    url = "https://api.trakt.tv/oauth/device/token"
    get_token_status = 0
		
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code
    }

    while get_token_status != 200:
        #Sleep for the default polling interval of 5 seconds
        time.sleep(5)
        
        #This is really sloppy right now. I'm basically
        #ignoring any status codes that aren't 200 and
        #I'm not stopping after the 300 second timeout
        r = requests.post(url, params=params, headers=headers)
        print(r.status_code)
        get_token_status = r.status_code
        if r.status_code == 200:

            output = json.loads(r.content)
            access_token = output["access_token"]
            refresh_token = output["refresh_token"]
            
            #Just printing out the tokens here which is dumb
            #but it serves my purposes temporarily
            print("Your access token is {}\nand your refresh token is {}".format(access_token, refresh_token))

if __name__ == '__main__':
    get_token(device_code())
