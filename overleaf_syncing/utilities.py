import os
from yaml import safe_dump, safe_load
from dropbox import Dropbox

def request_user_input(prompt: str) -> str:
    return input(prompt + ": ")


def search_for_file_in_parent_folders(target_file_name: str, search_file_path: str) -> str | None:
    for root, dirs, files in os.walk(search_file_path):
        if target_file_name in files:
            return os.path.join(root, target_file_name)
    return None

def create_yaml_file(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        safe_dump(data, file)


def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return safe_load(file)
    except FileNotFoundError:
        print("File not found in path: ", file_path)    
        return {}
    

def save_yaml_file(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        safe_dump(data, file, default_flow_style=False)
    

def create_new_config_file(file_path: str):
    data = {
        "synced_dirs": [],  # Use the correct key name and initialize as an empty list
        "app_key": "",
        "app_secret": "",
        "access_token": ""
    }
    save_yaml_file(file_path, data)






    


