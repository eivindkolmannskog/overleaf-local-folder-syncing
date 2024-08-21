import os
from yaml import safe_dump, safe_load
from dropbox import Dropbox
import urllib.parse


def request_user_input(prompt: str) -> str:
    return input(prompt + ": ")


def search_for_file_in_parent_folders(
    target_file_name: str, search_file_path: str
) -> str | None:
    for root, dirs, files in os.walk(search_file_path):
        if target_file_name in files:
            return os.path.join(root, target_file_name)
    return None


def create_yaml_file(file_path: str, data: dict):
    with open(file_path, "w") as file:
        safe_dump(data, file)


def load_yaml_file(file_path):
    try:
        with open(file_path, "r") as file:
            return safe_load(file)
    except FileNotFoundError:
        print("File not found in path: ", file_path)
        return {}


def save_yaml_file(file_path: str, data: dict):
    with open(file_path, "w") as file:
        safe_dump(data, file, default_flow_style=False)


def print_list_with_indexes(entry: list[str | int | float]):
    for index, item in enumerate(entry):
        print(f"{index:03} | {item}")


def request_app_secret() -> str:
    return request_user_input("Enter the app secret")


def request_app_key() -> str:
    return request_user_input("Enter the app key")


# def choose_overleaf_project(dropbox_client: Dropbox) -> str:
#    """
#    This function is used to choose an overleaf project in the clients dropbox, and return the directory as a string.
#    """
#    directory_chosen: bool = False
#    while not directory_chosen:
#        folders_data: dict = self.dropbox_client.files_list_folder(
#            path=self.directories.dropbox_sync_to_dir
#        ).entries
#        folder_names: list[str] = [obj.name for obj in folders_data]
#
#        print_list_with_indexes(folder_names)
#
#        root_dir: str = request_user_input(
#            "Choose a folder by inserting the index number"
#        )
#
#        print("You have chosen: ", folder_names[int(root_dir)])
#        self.directories.dropbox_sync_to_dir += "/" + folder_names[int(root_dir)]
#
#        sync_dir_chosen: str = request_user_input(
#            "Is this the directory you want to sync to? [Y/n]:"
#        )
#
#        if sync_dir_chosen.lower() is "y":
#            directory_chosen = True


def decode_url(url: str) -> str:
    parsed_url: str = urllib.parse.urlparse(url)
    decoded_path: str = urllib.parse.unquote(parsed_url.path)
    return decoded_path


def search_for_folders(folder_name, root_directory) -> list[str]:
    """
    Searches for folders with the given name in the root_directory and all subdirectories.
    """
    matching_folders = []
    
    # Walk through the root_directory
    for dirpath, dirnames, _ in os.walk(root_directory):
        # Check if the folder_name is in the list of directories
        if folder_name in dirnames:
            # Construct the full path to the matching folder and add to the list
            matching_folders.append(os.path.join(dirpath, folder_name))
    
    return matching_folders


