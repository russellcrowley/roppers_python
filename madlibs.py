#!/usr/bin/env python3
"""
madlibs.py - reads in a text file and replaces the following values:
ADJECTIVE
NOUN
VERB
with user defined text
Prints the output to the screen and saves to a new text file
"""
import re

file = input('enter your file name: ')
with open(file) as file:
    content = file.read()

check = re.compile(r'ADJECTIVE|VERB|NOUN')
changes = check.findall(content)

for word in changes:
    new_word = input('Enter a {}: '.format(word))
    content = content.replace(word, new_word)

print(content)
new_file = input('Enter the name of your new file: ')
with open(new_file, 'a') as new_file_write:
    new_file_write.write(content)

print('Thanks! your file has been saved as {}'.format (new_file))




