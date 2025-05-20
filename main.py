import os
import shutil

def organize_by_extension(root_dir):
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            # Skip directories created for extensions
            if foldername == root_dir and os.path.isdir(file_path):
                continue
            # Get the file extension
            _, ext = os.path.splitext(filename)
            ext = ext[1:].lower()  # remove the dot and lowercase
            if not ext:
                ext = "no_extension"

            # Create destination folder
            dest_folder = os.path.join(root_dir, ext)
            os.makedirs(dest_folder, exist_ok=True)

            # Destination file path
            dest_path = os.path.join(dest_folder, filename)

            # Move the file if it's not already in the destination folder
            if os.path.abspath(file_path) != os.path.abspath(dest_path):
                try:
                    shutil.move(file_path, dest_path)
                    print(f"Moved: {file_path} → {dest_path}")
                except Exception as e:
                    print(f"Failed to move {file_path}: {e}")

if __name__ == "__main__":
    target_directory = input("Enter the path to the directory to organize: ").strip()
    if os.path.isdir(target_directory):
        organize_by_extension(target_directory)
    else:
        print("Invalid directory.")
