from dropbox import Dropbox
import os
from .utilities import search_for_file_in_parent_folders, load_yaml_file, save_yaml_file, create_new_config_file, request_user_input
from .api_requests import send_folder_to_dropbox
from pprint import pprint


class SyncClient:

    def __init__(self):
        # TODO: Fix this: Set to the directory of the file that initializes the object manually now.
        #dir_of_object_initialization: str = os.path.dirname(os.path.absdir(__file__))
        dir_of_object_initialization: str = "/Users/eivindkolmannskog/overleaf-local-folder-syncing"

        
        self.is_authenticated: bool = False

        # Check if already configured, by looking for config.yaml in parent folders
        if search_for_file_in_parent_folders("config.yml", dir_of_object_initialization) is not None:
            print("Configuration found")
            self._config_file_path: str = os.path.join(search_for_file_in_parent_folders("config.yml", dir_of_object_initialization))
            self._set_configuration()
        else:
            print("Configuration not found")
            self._config_file_path: str = os.path.join(dir_of_object_initialization, "config.yml")
            create_new_config_file(self._config_file_path)
            self._set_configuration()
            self._request_secrets()
            self._save_configuration()


        # Set up a valid dropbox client
        while not self.is_authenticated:
            try:
                #access_token: str = fetch_access_token(self._app_key, self._app_secret)
                self.dropbox_client: Dropbox = Dropbox(oauth2_access_token=self._access_token, app_key=self._app_key, app_secret=self._app_secret)
                print("Authentication successful")
                self.is_authenticated = True
            except:
                print("Error: Unable to authenticate. Please try again")
                self._request_secrets()
                self._save_configuration()


        # Sync the directories
        if self.synced_dirs is not None:
            self._sync_directories()


    def _get_config_data(self):
        return load_yaml_file(self._config_file_path)

    def _set_configuration(self):
        config_data: dict = self._get_config_data()
        self.synced_dirs: list[str] = config_data.get("synced_dirs")
        self._app_secret: str = config_data.get("app_secret")
        self._app_key: str = config_data.get("app_key")
        self._access_token: str = config_data.get("access_token")
    
    def _request_secrets(self):
        self._app_key: str = request_user_input("Enter the app key")
        self._app_secret: str = request_user_input("Enter the app secret")
        self._access_token: str = request_user_input("Enter your access token")

    def _save_configuration(self):
        save_yaml_file(self._config_file_path, {"synced_dirs": self.synced_dirs, "app_key": self._app_key, "app_secret": self._app_secret, "access_token": self._access_token})

    def add_synced_dir(self, dir: str):
        #TODO:  Some validation to ensure the dir is valid

        # THIS IS DANGEROUS
        if dir not in self.synced_dirs:
            self.synced_dirs.append(dir)
        self._save_configuration()

    def _sync_directories(self):
        #for dir in self.synced_dirs:
            #send_folder_to_dropbox(self.dropbox_client, dir)
        
        # Dummy code: Send an empty tex file to dropbox
        #with open("test.txt", "r") as file:
            #file.read()
        folders_data: dict = self.dropbox_client.files_list_folder(path = "/Apper/overleaf").entries
        folder_names: list[str] = [obj.name for obj in folders_data]
        pprint(folder_names)

        #print(self.dropbox_)
        #self.dropbox_client.files_upload(path="apper/overleaf/Project Thesis", f=file)

    def reset() -> None:
        pass
        

    

    
    def __str__(self) -> str:
        return f"This is a SyncClient object"
    
