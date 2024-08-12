This is a tool for automatrically sync a folder within a dev environment with overleaf, going through Dropbox. This is perfect for scientific writing when plots generated locally needs to be able to be updated without the hassle of upload manually each time.



### Setup
First we need to set up a dropbox account or use an existing one, and with this account allow this app to be synced.

1. Go to https://www.dropbox.com/developers/apps and click "Create app", and follow the steps. This should give you an app key and an app secret, which we will need very soon.
2. Install the module using pip install



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

### Adding pre-commits
Assumes you ar navigated to the root repo folder. 
1. Open/create pre-commit file with:
    ```
    
    notepad .git/hooks/pre-commit
    
    ```

2. Edit the file with your commands, and save!
3. Make the pre-commit hook executable:
   ```

   git update-index --chmod=+x .git/hooks/pre-commit

   ```





