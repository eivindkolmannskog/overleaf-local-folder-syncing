from dropbox import Dropbox
import os
import requests
from dotenv import load_dotenv, set_key, unset_key
import webbrowser

class DropboxAPI:
    def __init__(self, project_folder_id: str, dotenv_path: str = '.env'):
        self.project_folder_id = project_folder_id
        self.dotenv_path = dotenv_path

        # Load existing environment variables from .env file
        load_dotenv(dotenv_path=self.dotenv_path)

        self.app_key = self.get_app_key()
        self.app_secret = self.get_app_secret()

        print("App key: " + self.app_key)
        print("App secret: " + self.app_secret)
        
        self.access_token = self.get_access_token()
        print("Access token: " + self.access_token)

        try:
            self.dbx = Dropbox(oauth2_access_token=self.access_token)
            print("Linked account: " + str(self.dbx.users_get_current_account()))
        except Exception as e:
            print(f"Error: Access token is invalid. {e}")

    def request_app_key_from_user(self) -> str:
        return input("Enter your app key: ")

    def request_app_secret_from_user(self) -> str:
        return input("Enter your app secret: ")

    def get_app_key(self):
        env_app_key = self.project_folder_id + "_APP_KEY"

        if env_app_key in os.environ:
            print("App key found in environmental variables")
            return os.environ[env_app_key]
        else:
            print("App key not found in environmental variables")
            app_key = self.request_app_key_from_user()
            set_key(self.dotenv_path, env_app_key, app_key)  # Save to .env file
            os.environ[env_app_key] = app_key
            return app_key
  
    def get_app_secret(self):
        env_app_secret = self.project_folder_id + "_APP_SECRET"

        if env_app_secret in os.environ:
            print("App secret found in environmental variables")
            return os.environ[env_app_secret]
        else:
            print("App secret not found in environmental variables")    
            app_secret = self.request_app_secret_from_user()
            set_key(self.dotenv_path, env_app_secret, app_secret)  # Save to .env file
            os.environ[env_app_secret] = app_secret
            return app_secret
        

    def get_access_token(self):
        
        REDIRECT_URI = 'https://localhost/'
        token_url = "https://api.dropboxapi.com/oauth2/token"
        REDIRECT_URI = "https://localhost/"
        auth_url = f"https://www.dropbox.com/oauth2/authorize?client_id={self.app_key}&response_type=code&redirect_uri={REDIRECT_URI}"
        webbrowser.open(auth_url)
        
        authorization_code = input("Enter the authorization code: ")
        
        data = {
            "code": authorization_code,
            "grant_type": "authorization_code",
            "client_id": self.app_key,
            "client_secret": self.app_secret,
            "redirect_uri": REDIRECT_URI,
        }

        response = requests.post(token_url, data=data)
        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            print("Error: Unable to obtain access token")
            print(response.json())
            return None


    def delete_environment_variables(self):
        env_app_key = self.project_folder_id + "_APP_KEY"
        env_app_secret = self.project_folder_id + "_APP_SECRET"

        if env_app_key in os.environ:
            unset_key(self.dotenv_path, env_app_key)  # Remove from .env file
            del os.environ[env_app_key]
        if env_app_secret in os.environ:
            unset_key(self.dotenv_path, env_app_secret)  # Remove from .env file
            del os.environ[env_app_secret]
