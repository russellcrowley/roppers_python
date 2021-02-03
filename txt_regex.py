#!/usr/bin/env python3
"""
Write a program that opens all .txt files in a folder and searches for 
any line that matches a user-supplied regular expression. The results 
should be printed to the screen.
"""
import os, re
def txt_regex():
    # set the folder to search
    directory = ospath.abspath(input("Type your folder path (y for current folder): "))
    search_term = re.compile(input("What is your search term? "))
    if directory.lower() == 'y':
        directory = os.getcwd()
    os.chdir(directory)
    # walk through a file
    for root, dirs, files in os.walk(directory):
        # if the file is txt
        for filename in files:
            if filename.endswith('.txt'):
                # open and then read the file
                file_content = open(directory + os.sep + filename, 'r')
                lines = file_content.readlines()
                for line in lines:
                    if re.findall(search_term, line):
                        print(line)
    print("Search concluded")

txt_regex()
            