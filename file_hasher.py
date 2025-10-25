import hashlib
import os 


def scan_folder(path):
     file_list = []
     for root, dirs, files in os.walk(path):
          for file in files:
               file_path = os.path.join(root, file)
               file_list.append(file_path)
     return file_list


def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()  



def hash_folder(path):
    files = scan_folder(path)
    for file in files:
        try:
            file_hash = hash_file(file)
            print(f"{file}: {file_hash}")
        except Exception as e:
            print(f"error reading or generating file {e}")




hash_folder("text")
    

