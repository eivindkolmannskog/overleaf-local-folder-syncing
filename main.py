from overleaf_syncing.api_requests import DropboxAPI


def main():
    api_client = DropboxAPI(project_folder_id="test_for_overleaf_syncing")
    #api_client.delete_environment_variables()

if __name__ == "__main__":
    main()