from overleaf_syncing.SyncClient import SyncClient

def main():
    sync_client = SyncClient()
    sync_client.remove_all_synced_folders()

    sync_client.add_synced_folder("results_1")
    sync_client.add_synced_folder("results_2")  
    

    print(sync_client)
    
    sync_client.sync()
    sync_client.erase_old_files()


if __name__ == "__main__":
    main()