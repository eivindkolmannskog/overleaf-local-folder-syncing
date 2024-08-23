from dropbox import Dropbox
import os
from .utilities import (
    request_user_input,
    decode_url,
    search_for_folders,
    dropbox_url_to_dropbox_path,
)
from .api_requests import upload_folder_to_dropbox
from pprint import pprint
from .DropboxOAuthHandler import DropboxOAuthHandler
from .ConfigurationHandler import ConfigurationHandler
from .Secrets import Secrets


class SyncClient:

    def __init__(self, reset: bool = False) -> None:

        if reset:
            self._reset()

        self.configuration: ConfigurationHandler = ConfigurationHandler(
            file_directory=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )

        self.secrets: Secrets = Secrets()
        while self.secrets.CLIENT_ACCESS_TOKEN is None:
            dropbox_oauth = DropboxOAuthHandler(
                self.secrets.CLIENT_APP_KEY, self.secrets.CLIENT_APP_SECRET
            )
            if dropbox_oauth.is_authorized():
                self.secrets.update_tokens(
                    dropbox_oauth.access_token, dropbox_oauth.refresh_token
                )
            else:
                print("Authorization failed. Trying again...")

        # Make a dropbox client
        try:
            self.dropbox_client: Dropbox = Dropbox(
                oauth2_access_token=self.secrets.CLIENT_ACCESS_TOKEN,
                oauth2_refresh_token=self.secrets.CLIENT_REFRESH_TOKEN,
                app_key=self.secrets.CLIENT_APP_KEY,
                app_secret=self.secrets.CLIENT_APP_SECRET,
            )
        except:
            raise Exception(
                "Could not create a Dropbox client. Please check your credentials."
            )

        if self.configuration.overleaf_project_directory is None:
            response: str = request_user_input(
                "Paste the URL of the dropbox URL you want to sync to"
            )
            self.set_overleaf_project(response)

    def set_overleaf_project(self, url: str) -> None:
        """
        Sets the overleaf project to the given URL if it is valid.
        """

        # Check if valid URL
        try:
            self.configuration.overleaf_project_directory = dropbox_url_to_dropbox_path(
                url
            )
            print(self.configuration.overleaf_project_directory)

            # This will fail if path does not exist
            self.dropbox_client.files_list_folder(
                path=self.configuration.overleaf_project_directory.lower()
            )

            self.configuration.save_config_file()
            print(
                f"Changed overleaf project to: {self.configuration.overleaf_project_directory}"
            )

        except:
            raise Exception("Invalid URL")

    def add_synced_folder(self, folder_name: str) -> None:
        # Search for folder in the project directory, and all subdirectories
        folder_paths = search_for_folders(
            folder_name, self.configuration.file_directory
        )
        filtered_folders = (
            ...
        )  # Filter out the folders that are subfolders that have the same name as the prent folder is eliminated
        if len(folder_paths) != 0:
            self.add_synced_directory(folder_paths)
        else:
            print(
                f"Folder {folder_name} not found in directory {self.configuration.file_directory}"
            )

    def remove_all_synced_folders(self) -> None:
        self.configuration.remove_all_synced_directories()

    def add_synced_directory(self, directory: str | list[str]) -> None:
        """
        Adds one directory to the synced directories list. If the directory input is a list, all directories will be added.
        """
        if isinstance(directory, str):
            # Handle for single directory
            self.configuration.synced_directories.append(directory)

        elif isinstance(directory, list):
            # Handle for multiple directories'
            for dir in directory:
                self.configuration.synced_directories.append(dir)
        else:
            raise Exception("Invalid input type for directory")

    def upload_synced_folders(self) -> None:
        """
        Uploads the selected folders with the overleaf project, through dropbox.
        """

        for directory in self.configuration.synced_directories:
            upload_folder_to_dropbox(
                self.dropbox_client,
                directory,
                self.configuration.overleaf_project_directory.lower(),
            ),

    def erase_unmatched_files(self) -> None:
        """
        Erases files in the overleaf project that are not in the local synced directories. The SyncClient.upload() method only uploads
        """

    def sync(self) -> None:
        """
        Syncing the selected folders with the overleaf project, through dropbox.
        """
        print("Syncing...")
        self.upload_synced_folders()
        self.erase_unmatched_files()
        print("Syncing complete!")

    def _reset(self) -> None:
        # Delete the config file
        try:
            print(os.path.join(self.configuration.file_directory, "config.yml"))
            os.remove(os.path.join(self.configuration.file_directory, "config.yml"))
        except:
            print("Config file already deleted")

        try:
            os.remove(".env")
        except:
            print(".env file already deleted")

        try:
            os.environ.pop("CLIENT_APP_KEY", None)
            os.environ.pop("CLIENT_APP_SECRET", None)
            os.environ.pop("CLIENT_ACCESS_TOKEN", None)
            os.environ.pop("CLIENT_REFRESH_TOKEN", None)
        except:
            print("Environment variables already deleted")

        print("Reset complete!")

    def __str__(self) -> str:
        return f"SyncClient is connected with dropbox account, {self.dropbox_client.users_get_current_account().name.display_name}, {self.dropbox_client.users_get_current_account().email}"
