# SHA-256 File Hasher & Duplicate Finder

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Stable-success)

A **lightweight, modular Python tool** to:
- Recursively scan folders
- Compute **SHA-256 hashes** for all files
- Detect **exact duplicates** by content
- Provide a **clean API** for developers

Zero dependencies. Easy to integrate.

---

## Features

- Recursive folder scanning
- Secure SHA-256 hashing (64KB chunks)
- Duplicate detection by file content
- Clean, object-oriented API
- Ready-to-use example script
- No external packages required

---

## Installation

```bash
git clone https://github.com/dillionhuston/SHA-256-File-Hasher.git
cd SHA-256-File-Hasher
```
- No requirements.txt needed — pure Python!

- ## Folder Structure
```bash
  sha256-duplicate-finder
│
├── API/
│   ├── __init__.py
│   ├── API.py            # Main API entry point
│   ├── HashFile.py       # SHA-256 file hasher
│   ├── ScanFolder.py     # Recursive folder scanner
│   ├── FolderHandler.py  # Hash all files in folder
│   └── DuplicateFinder.py # Detect duplicate groups
│
├── usage.py              # Example usage
└── README.md
```

## Quick Start API
```python
from API.API import FileHasherAPI

# Initialize with folder path
api = FileHasherAPI("path/to/your/folder")

# Get all file hashes
hashes = api.get_hashes()
# → { "file1.txt": "a1b2c3...", "file2.txt": "a1b2c3..." }

# Get only duplicates
duplicates = api.get_duplicates()
# → { "a1b2c3...": ["file1.txt", "copy/file1.txt"] }
```

## Example output
```text
All file hashes:
text/file1.txt: d179aeebdc32f0d8a2...
text/file2.txt: d179aeebdc32f0d8a2...
text/unique.txt: 8bc74a21e3f14c9d...

Duplicates found:
Hash: d179aeebdc32f0d8a2...
 - text/file1.txt
 - text/file2.txt
```

## Run the example
```bash
python usage.py
```


---

## How It Works (Technical)

1. **`ScanFolder.scan_folder(folder_path)`**  
   - Uses `os.walk()` to recursively traverse the directory.  
   - Collects **absolute paths** of all files (ignores directories).  
   - Returns a flat list of file paths.

2. **`HashFile.hash_file()`**  
   - Opens file in binary mode (`'rb'`).  
   - Reads in **64KB chunks** to support large files efficiently.  
   - Updates `hashlib.sha256()` hasher incrementally.  
   - Returns **hex digest** (64-character string).

3. **`FolderHandler.hash_folder()`**  
   - Scans folder → gets file list.  
   - For each file:  
     - Instantiates `HashHandler(file_path)`  
     - Computes hash  
     - Builds a **reverse map**: `{hash: [file_path, ...]}`  
   - Prints progress (optional)  
   - **Returns the full hash map**

4. **`DuplicateFinder.find_duplicates(hash_dict)`**  
   - Iterates over the hash map.  
   - Filters groups where `len(files) > 1`.  
   - Returns **only duplicate groups**  
   - Prints human-readable summary

5. **`FileHasherAPI`**  
   - Public interface  
   - `get_hashes()` → returns full `{file: hash}` map  
   - `get_duplicates()` → returns only duplicate groups  
   - **No side effects** beyond optional prints

---

> **Thread-safe?** No — uses standard file I/O.  
> **Memory usage?** Stores all file paths and hashes in memory.  
> **Large files?** Yes — streams in 64KB chunks.  
> **Zero dependencies** — pure `stdlib`.

---

## Use Cases

- Clean up duplicate photos, documents, or backups
- Audit datasets for redundancy
- Integrate into backup/sync tools
- Pre-process data for ML pipelines

---

## Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push & open a Pull Request

---

## License

[MIT License](LICENSE) – Free to use, modify, and distribute.

---

## Author

**Dillon Huston**  
[GitHub Profile](https://github.com/dillionhuston)

---

> **Small. Fast. Reliable.**  
> *Find duplicates. Save space. Code smarter.*

  
