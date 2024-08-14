#import requests
#import webbrowser
from dropbox import Dropbox
import os
#
#
#def fetch_access_token(app_key: str, app_secret: str) -> str:
#        
#    REDIRECT_URI = 'https://localhost/'
#    TOKEN_URL = "https://api.dropboxapi.com/oauth2/token"
#    AUTHENTICATION_URL = f"https://www.dropbox.com/oauth2/authorize?client_id={app_key}&response_type=code&redirect_uri={REDIRECT_URI}"
#    webbrowser.open(AUTHENTICATION_URL)
#    
#    ### This needs to be fetched automatically
#    authorization_code = input("Enter the authorization code: ")
#    
#    data = {
#        "code": authorization_code,
#        "grant_type": "authorization_code",
#        "client_id": app_key,
#        "client_secret": app_secret,
#        "redirect_uri": REDIRECT_URI,
#    }
#
#    response = requests.post(TOKEN_URL, data=data)
#    if response.status_code == 200:
#        print(response.json())
#        return response.json()["access_token"]
#    else:
#        print("Error: Unable to obtain access token")
#        print(response.json())
#        return None


#import requests
#import webbrowser
#from flask import Flask, request
#import threading
#
#app = Flask(__name__)
#
## Global variable to store the authorization code
#authorization_code = None
#
#@app.route('/')
#def get_authorization_code():
#    global authorization_code
#    authorization_code = request.args.get('code')  # Get the authorization code from the query parameters
#    return "Authorization code received! You can close this window now."
#
#def start_local_server():
#    app.run(port=5000)
#
#def fetch_access_token(app_key: str, app_secret: str) -> str:
#    global authorization_code
#
#    REDIRECT_URI = 'http://localhost:5000/'
#    TOKEN_URL = "https://api.dropboxapi.com/oauth2/token"
#    AUTHENTICATION_URL = f"https://www.dropbox.com/oauth2/authorize?client_id={app_key}&response_type=code&redirect_uri={REDIRECT_URI}"
#
#    # Start a thread for Flask server
#    threading.Thread(target=start_local_server).start()
#
#    # Open the Dropbox authorization URL
#    webbrowser.open(AUTHENTICATION_URL)
#    
#    # Wait until the authorization code is received
#    while authorization_code is None:
#        pass  # Busy wait for the code (better to implement a proper wait)
#
#    # Exchange the authorization code for an access token
#    data = {
#        "code": authorization_code,
#        "grant_type": "authorization_code",
#        "client_id": app_key,
#        "client_secret": app_secret,
#        "redirect_uri": REDIRECT_URI,
#    }
#
#    response = requests.post(TOKEN_URL, data=data)
#    if response.status_code == 200:
#        print(response.json())
#        return response.json()["access_token"]
#    else:
#        print("Error: Unable to obtain access token")
#        print(response.json())
#        return None

    
def send_folder_to_dropbox(dropbox_client: Dropbox, folder_path: str) -> None:
    for file in os.listdir(folder_path):
        with open(f"{folder_path}/{file}", 'r') as file:
            file_content = file.read()
            dropbox_client.files_upload(file_content, f"/{folder_path}/{file}")







