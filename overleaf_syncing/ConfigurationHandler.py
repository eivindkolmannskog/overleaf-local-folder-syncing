import os
from .utilities import load_yaml_file, save_yaml_file, search_for_file_in_parent_folders


class ConfigurationHandler:
    def __init__(self, file_directory: str):

        config_file_path = self.file_directory = search_for_file_in_parent_folders(
                target_file_name="config.yml", search_file_path=file_directory
            )
        
        if config_file_path is not None:
            self.file_directory = os.path.dirname(config_file_path)
        else:
            self.file_directory = file_directory
            self.synced_directories = []
            self.overleaf_project_directory = None
            self.save_config_file()
        
        self.load_config_file()

        print(self.__dict__)

    def save_config_file(self) -> None:
        """
        Saves the configuration data from member variables to the config file in the file directory.
        """
        data = {
            "synced_directories": self.synced_directories,
            "overleaf_project_directory": self.overleaf_project_directory,
        }
        save_yaml_file(os.path.join(self.file_directory, "config.yml"), data)

    def load_config_file(self) -> None:
        """
        Loads the config file from the file directory, and assign the data to member variables.
        """
        config_data: dict = load_yaml_file(
            os.path.join(self.file_directory, "config.yml")
        )

        self.synced_directories = config_data.get("synced_directories")
        self.overleaf_project_directory = config_data.get("overleaf_project_directory")


    def add_synced_directory(self, directory: str) -> None:
        if directory not in self.synced_directories:
            self.synced_directories.append(directory)
            self.save_config_file()
            
