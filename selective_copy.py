#!/usr/bin/env python3
"""
Write a program that walks through a folder tree and searches for files with a certain file extension 
(such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
"""
import shutil, os, re
from pathlib import Path
def selective_copy():
     # set the folder to search
    directory = os.path.abspath(input("Type your folder path to search (y for current folder)\n"))
    if directory.lower() == 'y':
        directory = os.getcwd()
    search_term = input("What file extension are you looking for? Include the '.'!\n")
    folder_name = os.path.abspath(input("""Name the folder to copy your results into, 'y' for current directory
    (a new folder will be created if this doesn't already exist)\n"""))
    if folder_name.lower() == 'y':
        folder_name = os.getcwd()
    elif not os.path.exists(folder_name):
        os.makedirs(folder_name)
    # walk through a file
    for root, dirs, files in os.walk(directory):
        # if the file suffix matches the terms
        for filename in files:
            if filename.endswith(search_term):
                # copy it into the results folder
                try:
                    print(f"Copying {filename}...")
                    shutil.copy((os.path.join(path, root, filename)), f"{folder_name}")
                    # shutil.copy(f"{root}\{filename}", f"{folder_name}")
                # ignore files already in the result folder
                except shutil.SameFileError:
                    continue
    print(f"Search concluded, results in {folder_name}")

selective_copy()