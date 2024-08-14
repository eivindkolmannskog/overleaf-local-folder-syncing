from overleaf_syncing.SyncClient import SyncClient

def main():
    sync_client = SyncClient()

    sync_client.add_synced_dir("/Users/eivindkolmannskog/overleaf-local-folder-syncing/dummyfolder")



if __name__ == "__main__":
    main()