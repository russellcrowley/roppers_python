#!/usr/bin/env python3
"""
Write a program that walks through a folder tree and searches for exceptionally large files
or folders—say, ones that have a file size of more than 100MB.
(Remember that to get a file’s size, you can use os.path.getsize() from the os module.)
 these files with their absolute path to the screen.
 """
import os
def file_size():
    # get the folder from the user
    temp = input("Type your folder path to search (y for current folder)\n")
    if temp.lower() == 'y':
        directory = os.getcwd()
    else:
        directory = os.path.abspath(temp)
    print(directory)
    # get the size to look for
    size_check = int(input("In MB, what size do you want to find files over?: "))
    # walk through the folder
    for root, dirs, files in os.walk(directory):
        for filename in files:
            try:
                # get size of file and convert to MB
                size = (os.path.getsize(os.path.join(root, filename)))/(1024*1024)
                # if the file is above the size, print it
                if size > size_check:
                    print("{} is {:.2f} MB".format(filename, size))
            # skip strange/hidden files
            except FileNotFoundError:
                pass
    print("Size check complete")

file_size()
