# Extract XISO and Rename in Batch

__author__ = 'Joyway'
__version__ = '1.0'

import json
import os
import zlib
from subprocess import run


repack_list = []
with open('RepackList.json') as f:
    repack_list = json.load(f)
with open('AltRepackList.json') as f:
    repack_list += json.load(f)

def get_xiso_directory():
    xiso_list = []
    xiso_directory = ''
    while True:
        raw_path = input('# Enter the path of the XISOs source directory: ')
        if not os.path.exists(raw_path.strip()):
            print('# The path does NOT exist!')
            continue
        file_list = os.listdir(raw_path.strip())
        for file in file_list:
            if file[-4:] == '.iso':
                xiso_list.append(file)
        if not xiso_list:
            print('# The directory does NOT contain any ISO!')
            continue
        xiso_source = raw_path.strip()
        return xiso_source, xiso_list

def get_output_directory():
    while True:
        raw_path = input('# Enter the path of the output directory: ')
        if not os.path.exists(raw_path.strip()):
            print('# The path does NOT exist!')
            continue
        output_directory = raw_path.strip()
        return output_directory
    
def get_folder_name(xiso_checksum):
    global repack_list
    for game in repack_list:
        if game['ISO Checksum'] == xiso_checksum:
            folder_name = game['Folder Name']
            return folder_name
    else:
        return False

def crc_checksum(file):
    with open(file, 'rb') as f:
        checksum = f'{zlib.crc32(f.read()):0>8X}'
    return checksum
    
def extract_xiso(xiso_source, xiso_file, output_directory):
    xiso_path = os.path.join(xiso_source, xiso_file)
    xiso_checksum = crc_checksum(xiso_path).strip()
    folder_name = get_folder_name(xiso_checksum)
    if not folder_name:
        print(f'Checksum not found!', end='')
    else:
        game_path = os.path.join(output_directory, folder_name)
        if os.path.exists(game_path):
            print(f'Already exists!', end='')
        else:
            print(f'Extracting...', end='')
            run(['extract-xiso.exe', '-q', '-d', game_path, xiso_path])

def main():
    print('# Welcome!\n')
    xiso_source, xiso_list = get_xiso_directory()
    output_directory = get_output_directory()
    total_count = len(xiso_list)
    padding = len(str(total_count))
    for i, xiso_file in enumerate(xiso_list):
        print(f'\n# ({i + 1:0{padding}}/{len(xiso_list)}) {xiso_file}: Verifying...', end=' ')
        extract_xiso(xiso_source, xiso_file, output_directory)

if __name__ == '__main__':
    main()