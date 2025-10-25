from API.FolderHandler import FolderHandler
from API.DuplicateFinder import DuplicateFinder
class FileHasherAPI:
    def __init__(self, folder_path):
        self.folder_handler = FolderHandler(folder_path)
        self.duplicates_handler = DuplicateFinder()

    def get_hashes(self):
        """Return dict of {file_path: file_hash}"""
        return self.folder_handler.hash_folder()

    def get_duplicates(self):
        """Return dict of duplicates {hash: [file_paths]}"""
        hashes = self.get_hashes()
        return self.duplicates_handler.find_duplicates(hashes)
