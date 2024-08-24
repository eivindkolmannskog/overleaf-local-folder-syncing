This is a tool for automatrically sync a folder within a dev environment with overleaf, going through Dropbox. This is perfect for scientific writing when plots generated locally needs to be able to be updated without the hassle of upload manually each time. To use it, you use this project as a python module locally, and connect your desired dropbox account 
This project is still under development, and may be prone to errors.

### Setup
First we need to set up a dropbox account or use an existing one, and with this account allow this app to be synced.
1. Sync Overleaf with Dropbox (requires a paid overleaf account). Follow the instructions given by Overleaf [here](https://www.overleaf.com/learn/how-to/Dropbox_Synchronization).
2. Go to https://www.dropbox.com/developers/apps and click "Create app", and choose the options shown below. You can name your app anything you wish.
   ![image](https://github.com/user-attachments/assets/26a07f75-4417-4f5c-9c90-f10a94424415)
   Then click "Create app" again

4. In settings tab, set the redirect URl to be
   ```
   http://localhost:5000/oauth/callback in settings
   ```
   ![image](https://github.com/user-attachments/assets/76c120ce-92ef-43d6-b3e4-bf62e5b65f57)
   Also note that this page shows an "App key" and an "App secret". Those will be needed soon.
6. In "permissions" tab, set the permissions as shown below:
   ![image](https://github.com/user-attachments/assets/5d5964fb-def3-4b0a-8076-7f3d64235d01)

7. In your local project folder on yur computer, install the module with pip:
   ```
   pip install "git+https://github.com/eivindkolmannskog/overleaf-local-folder-syncing.git@main#egg=OverleafSyncing"
   ```
   It is recommended to use a virtual environment.

8. Make a new .py file in the root directory of your local project folder, and paste in
   ```python
   import os
   from overleaf_syncing.OverleafSyncing import OverleafSyncing

   # Dropbox URL of your Overleaf project:
   DROPBOX_URL = "https://www.dropbox.com/url/of/your/overleaf/project"
   # Root of your project directory, which will be the directory of this file.
   root_dir: str = os.path.dirname(__file__)

   # Create a client
   client = OverleafSyncing(dropbox_url=DROPBOX_URL)

   # Define paths we want to sync. You can create as many as you want
   synced_folder_1: str = os.path.join(root_dir, "<your_folder_name>")
   client.add_synced_directories(synced_folder_1)

   # Upload the folders to the Overleaf project
   client.upload_synced_folders()
   ```
When you run this, the configuration will start. You will here need to paste in your app key and app secret which was given in step 4. Also the dropbox url of your project needs to be provided, and you will find it by navigating to your dropfox folder in your web browser. e.g https://www.dropbox.com/home/Apper/Overleaf/Project%20Thesis, where the project folder is called "Project Thesis". You will also be redirected to your browser to accept that your app is connecting to your dropbox.

This script will be extended later, and how to set up the syncing will be explained in "Usage" below.


### Usage
When your app and script is set up as described in "Setup", only thing you will have to do is to run your script.

   ```python
   import os
   from overleaf_syncing.SyncClient import SyncClient

   # Create a client
   client = SyncClient()

   # Root of the project directory, which will be the location of this file
   root = os.path.dirname(__file__)

   # Define paths we want to sync. You can create as many as you want
   path_1 = os.path.join(root, "<folder_name_1>")
   path_2 = os.path.join(root, "<folder_name_2>")

   # Tell the client to sync the defined paths.
   # Either give a list of paths or a single path.
   client.add_synced_directory([path_1, path_2])

   # Upload the folders to the Overleaf project
   client.upload_synced_folders()
   ```

###Examples

### Contribute
1. Clone repository locally.
2. Navigate to the folder where you saved it.
3. Make a virtual environment:
    ```

    python -m venv venv

    ```

4. Activate environment:
   ```

   venv/scripts/activate

   ```

6. Install dependencies.

   ```
   
   pip install -r requirements.txt
   
   ```
   





