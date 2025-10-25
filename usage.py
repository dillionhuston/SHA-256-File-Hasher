from API.API import FileHasherAPI
folder = "text"
api = FileHasherAPI(folder)

# Get all hashes
hashes = api.get_hashes()
print("All file hashes:")

for file_path, file_hash in hashes.items():
    print(f"{file_path}: {file_hash}")

# Get duplicates
duplicates = api.get_duplicates()
print("\nDuplicates found:")

for file_hash, files in duplicates.items():
    print(f"Hash: {file_hash}")
    for f in files:
        print(f" - {f}")
