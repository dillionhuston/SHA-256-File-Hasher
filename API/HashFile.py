import hashlib

class HashHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.hasher = hashlib.sha256()

    def hash_file(self):
        with open(self.file_path, 'rb') as f:
            while chunk := f.read(65536):
             self.hasher.update(chunk)
        return self.hasher.hexdigest()
