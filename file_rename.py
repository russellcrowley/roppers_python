#!/usr/bin/env python3
"""
Write a program that finds all files with a given prefix, 
such as spam001.txt, spam002.txt, and so on, in a single folder 
and locates any gaps in the numbering (such as if there is a spam001.txt a
nd spam003.txt but no spam002.txt). Have the program rename all the 
later files to close this gap.
"""
import os, re
# select folder to be searched
temp = input("Type your folder path to search (y for current folder)\n")
if temp.lower() == 'y':
    directory = os.getcwd()
else:
    directory = os.path.abspath(temp)
# select prefix to be searched
prefix = input("What file prefix do you want to be found and numbered? ")
# set file number count
file_number = 1
# walk through files in folder
for root, dir, files in os.walk(directory):
# walk through the files
    for filename in sorted(files):
        if filename.startswith(prefix):
            # construct new filename
            not_used, suffix = filename.split(".")
            new_filename = prefix + str(file_number).zfill(3) + "." + suffix
            os.rename(os.path.join(directory, filename), 
            os.path.join(directory, new_filename))
            # increment the filename count
            file_number += 1
            print("Renamed {} to {}".format(filename, new_filename))
        else:
            pass
    print("File renaming complete!")

"""
Notes:
-I got hung up on regex before realising I didn't need to
-Be careful when reusing variables - I used 'prefix' twice
-I forgot to use os.path.join on the rename function
-Looking up the zfill function was really useful for naming

Poss future ideas:
-Argument to insert a break into some numbered files
-Take in extra arguments to rename more than one prefix
"""