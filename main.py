import os
from src.overleaf_syncing.OverleafSyncing import OverleafSyncing

def main():
    client = OverleafSyncing(dropbox_url="https://www.dropbox.com/home/Apper/Overleaf/Project%20Thesis")

    root = os.path.dirname(os.path.abspath(__file__))

    path_1 = os.path.join(root, "mock", "results_1")
    path_2 = os.path.join(root, "mock", "results_2")
    client.add_synced_directories(path_1)
    client.add_synced_directories(path_2)

    client.upload_synced_folders()



if __name__ == "__main__":
    main()