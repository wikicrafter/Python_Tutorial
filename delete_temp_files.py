import os
import shutil

def delete_temp_items():
    """Deletes all temporary files and folders from the Windows OS."""

    # Get the path of the temporary directory
    temp_dir = os.environ["TEMP"]

    # Lists to store deleted items and items that encountered errors
    deleted_items = []
    error_items = []

    # Delete temporary files
    temp_files = os.listdir(temp_dir)
    for temp_file in temp_files:
        try:
            file_path = os.path.join(temp_dir, temp_file)
            os.remove(file_path)
            deleted_items.append(temp_file)
        except PermissionError:
            error_items.append(temp_file)

    # Delete temporary folders
    temp_folders = [folder for folder in os.listdir(temp_dir) if os.path.isdir(os.path.join(temp_dir, folder))]
    for temp_folder in temp_folders:
        try:
            folder_path = os.path.join(temp_dir, temp_folder)
            shutil.rmtree(folder_path)
            deleted_items.append(temp_folder + "/")  # Append "/" to indicate it's a folder
        except PermissionError:
            error_items.append(temp_folder + "/")

    # Print the deleted items
    print("Deleted items:")
    for item_name in deleted_items:
        print(item_name)

    # Print the items that encountered errors
    print("Items that encountered errors:")
    for item_name in error_items:
        print(item_name)

if __name__ == "__main__":
    delete_temp_items()
