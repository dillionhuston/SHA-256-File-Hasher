import hashlib
def hash_file(path):
    hash = hashlib.sha256()

    while True:
            with open(path, "rb") as f:
                while chunk:= f.read(65536):
                 if not chunk:
                        break
                hash.update(chunk)
            return hash.digest()

                
print(hash_file("file.txt"))