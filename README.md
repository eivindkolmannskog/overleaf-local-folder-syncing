This is a tool for automatrically sync a folder within a dev environment with overleaf, going through Dropbox. This is perfect for scientific writing when plots generated locally needs to be able to be updated without the hassle of upload manually each time.




### Setup
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





