This is a tool for automatrically sync a folder within a dev environment with overleaf, going through Dropbox. This is perfect for scientific writing when plots generated locally needs to be able to be updated without the hassle of upload manually each time. To use it, you use this project as a python module locally, and connect your desired dropbox account 



### Setup
First we need to set up a dropbox account or use an existing one, and with this account allow this app to be synced.
1. Sync Overleaf with Dropbox (requires a paid overleaf account)
2. In your local project folder, install the module with pip:
   ```

   pip install "git+https://github.com/eivindkolmannskog/overleaf-local-folder-syncing.git"

   ```
   It is recommended to use a virtual environment.
   
3. Go to https://www.dropbox.com/developers/apps and click "Create app", and follow the steps. This should give you an app key and an app secret, which we will need very soon.



### Usage

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
   





