from src.overleaf_syncing.SyncClient import SyncClient

def main():
    sync_client = SyncClient(reset=True)
    #sync_client.remove_all_synced_folders()

    #sync_client.add_synced_folder("results_1")
    #sync_client.add_synced_folder("results_2")  
    
    #sync_client.upload_synced_folders()



if __name__ == "__main__":
    main()