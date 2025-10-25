import hashlib
import os 


def check_duplicates(hash_dict):
    duplicates_found = False
    no_dupicates = 0

    for file_hash, files in hash_dict.items():
        if len(files) > 1:
            duplicates_found = True
            print("duplicates found")

            for file in files:
                print(f" -  {file}")
                no_dupicates += len(files) - 1 

    if not no_dupicates:
        print("no duplicates found")
    else:
        print(f"Duplicates found {no_dupicates}")



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
    hash_dict = {}
    files = scan_folder(path)

    for file in files:
        try:
            file_hash = hash_file(file)

            if file_hash in hash_dict:
                hash_dict[file_hash].append(file)
            else:
                hash_dict[file_hash] = [file] 
            print(f"{file}: {file_hash}")
            check_duplicates(hash_dict)

        except Exception as e:
            print(f"error reading or generating file {e}")




hash_folder("text")

    

