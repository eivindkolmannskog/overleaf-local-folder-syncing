from dropbox import Dropbox
import dropbox
import os


def sanitize_path(path: str) -> str:
    # Replace backslashes with forward slashes and remove redundant './'
    path = path.replace("\\", "/").replace("//", "/")
    # Remove any './' occurrences
    path = path.replace("/./", "/")
    # Ensure path starts with a slash
    if not path.startswith("/"):
        path = "/" + path
    # Remove trailing slashes if present
    if path.endswith("/"):
        path = path.rstrip("/")
    return path



def upload_folder_to_dropbox(dbx: Dropbox, local_folder: str, dropbox_folder: str):
    for root, dirs, files in os.walk(local_folder):
        relative_path = os.path.relpath(root, local_folder)
        dropbox_path = sanitize_path(dropbox_folder + "/" + relative_path)

        if relative_path != ".":
            try:
                dbx.files_create_folder_v2(dropbox_path)
            except dropbox.exceptions.ApiError as err:
                if err.error.is_path() and err.error.get_path().is_conflict():
                    pass
                else:
                    raise

        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            dropbox_file_path = sanitize_path(dropbox_path + "/" + file_name)

            try:
                with open(local_file_path, "rb") as f:
                    dbx.files_upload(
                        f.read(), dropbox_file_path, mode=dropbox.files.WriteMode.overwrite
                    )
                print(f"Uploaded {local_file_path} to {dropbox_file_path}")
            except dropbox.exceptions.ApiError as e:
                print(f"Failed to upload {local_file_path} to {dropbox_file_path}: {e}")


