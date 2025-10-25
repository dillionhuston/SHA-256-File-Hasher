import os
class ScanFolder:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def scan_folder(self):
         
         file_list = []
         for root, dirs, files in os.walk(self):
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
         return file_list