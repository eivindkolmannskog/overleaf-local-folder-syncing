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
from .Secrets import Secrets


class OverleafSyncing:

    def __init__(self, *, dropbox_url: str, reset: bool = False) -> None:

        if reset:
            self._reset()

        self.synced_directories: list[str] = []
        self.secrets: Secrets = Secrets()

        # Run until authenticated
        while self.secrets.CLIENT_ACCESS_TOKEN is None:
            dropbox_oauth = DropboxOAuthHandler(
                self.secrets.CLIENT_APP_KEY, self.secrets.CLIENT_APP_SECRET
            )
            if dropbox_oauth.is_authorized():
                self.secrets.update_tokens(
                    dropbox_oauth.access_token, dropbox_oauth.refresh_token
                )
            else:
                raise Exception("Failed to authenticate with Dropbox")

        # Make a dropbox client
        try:
            self.dropbox_client: Dropbox = Dropbox(
                oauth2_access_token=self.secrets.CLIENT_ACCESS_TOKEN,
                oauth2_refresh_token=self.secrets.CLIENT_REFRESH_TOKEN,
                app_key=self.secrets.CLIENT_APP_KEY,
                app_secret=self.secrets.CLIENT_APP_SECRET,
            )
        except:
            self._reset()
            raise Exception(
                "Could not create a Dropbox client. Please check your credentials."
            )

        try:
            self.overleaf_project_directory = dropbox_url_to_dropbox_path(dropbox_url)
            # This will fail if path does not exist
            self.dropbox_client.files_list_folder(path=self.overleaf_project_directory)
        except:
            raise Exception("Invalid dropbox URL provided")

    def add_synced_directories(self, directories: str | list[str]) -> None:
        """
        Adds one or more directories to the synced directories list.
        If the directory input is a list, all directories will be added.
        Ensures that no duplicates are added to the list.
        """
        if isinstance(directories, str):
            directories = [directories]  # Convert single directory to a list

        [
            self.synced_directories.append(dir)
            for dir in directories
            if dir not in self.synced_directories
        ]

    def upload_synced_folders(self) -> None:
        """
        Uploads the selected folders with the overleaf project, through dropbox.
        """

        for directory in self.synced_directories:
            upload_folder_to_dropbox(
                self.dropbox_client,
                directory,
                self.overleaf_project_directory,
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
