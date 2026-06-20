# Task 3 - Task Automation with Python Scripts

## Overview
A Python automation script that organizes image files by scanning a source folder and moving all `.jpg` files into a destination folder. This demonstrates basic file-handling automation using Python's `os` and `shutil` modules.

## How It Works
1. Defines a **source directory** (`Game images`) to scan for `.jpg` files.
2. Defines a **destination directory** (`image`) where matching files will be moved.
3. Creates the destination folder automatically if it doesn't already exist.
4. Iterates through all files in the source folder, identifies files ending in `.jpg` (case-insensitive), and moves each one to the destination folder.
5. Prints a log of every file moved and a final summary of how many files were processed.

## File
- `Task 3.py` - Main automation script.

## Folders
- `Game images/` - Source folder containing the original `.jpg` screenshots.
- `image/` - Destination folder where `.jpg` files are moved to.

## How to Run
```bash
python "Task 3.py"
```

> **Note:** The script uses hardcoded local file paths (`SOURCE_DIR` and `DEST_DIR`) pointing to a specific machine's folder structure. Update these paths in the script to match your own environment before running.

## Sample Output
```
Scanning folder: C:\Users\mahee\pythonproject\...\Game images

Moved: Screenshot (1763).jpg → C:\Users\mahee\pythonproject\...\image
Moved: Screenshot (1764).jpg → C:\Users\mahee\pythonproject\...\image
...

Done! 5 .jpg file(s) moved.
```

## Notes
- Built entirely with Python's standard library (`os`, `shutil`) - no external dependencies.
- Designed as a simple file-organization automation example; the same pattern can be adapted for other automation tasks like email extraction or web scraping.
