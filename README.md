# Extract and Rename XISOs(Xbox OG)

Extract contents from Xbox Original ISOs to HDD ready folders and rename the folders based on FATX naming convention.

This is my personal script for my personal softmodded Xbox OG, please use [Team Resurgent's Repackinator](https://github.com/Team-Resurgent/Repackinator) if you want a more powerful ISO manager.


## Prerequisite

- Python 3.6+
- `RepackList.json` and `AltRepackList.json` from https://github.com/Team-Resurgent/Repackinator/
- The `extract-xiso.exe` from https://github.com/XboxDev/extract-xiso

## Initial Setup

1. Download and install Python 3.6+
2. Download the project from Github and extract it
3. Download and put following files into the root directory of this script:
    - RepackList.json
    - AltRepackList.json
    - extract-xiso.exe

## How to use    
Run the script in terminal: `python3 extract_xiso_batch.py`

## How does it work
Very simple! It calculates the checksum of the ISOs then get the folder name from `RepackList.json` and `AltRepackList.json`, after that, it uses `extract-xiso.exe` to extract the iso.

## Known Issues:
- Some games may contain files with long filename that exceeds the limit of FATX filesystem(42 characters). In that case, just use Repackinator to create the hdd-ready version game...