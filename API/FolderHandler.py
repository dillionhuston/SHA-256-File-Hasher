import os
from API.HashFile import HashHandler
from API.ScanFolder import ScanFolder

class FolderHandler:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def hash_folder(self):
        """
        Hash all files in folder and return dict: {file_path: hash}
        """
        file_list = ScanFolder.scan_folder(self.folder_path)
        hash_dict = {}

        for file in file_list:
            try:
                file_hash = HashHandler(file).hash_file()
                hash_dict.setdefault(file_hash, []).append(file)
                print(f"{file}: {file_hash}")
            except Exception as e:
                print(f"Error hashing {file}: {e}")

        return hash_dict

