class DuplicateFinder:
    @staticmethod
    def find_duplicates(hash_dict):
        duplicates = {}  
        total_duplicates = 0

        for file_hash, files in hash_dict.items():
            if len(files) > 1:
                duplicates[file_hash] = files
                print("found duplicates")
                for file in files:
                    print(f"file: {file}")
                total_duplicates += len(files) - 1

        if not duplicates:
            print("No duplicates found")
        else:
            print(f"Found {total_duplicates} duplicate files")

        return duplicates  
