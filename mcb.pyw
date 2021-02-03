#!/usr/bin/env python3

"""
mcb.pyw - Saves, loads and deletes pieces of text to the clipboard
Usage
python mcb.pyw save <keyword> - Saves clipboard to keyword.
python mcb.pyw <keyword> - Loads keyword to clipboard.
python mcb.pyw list - Loads all keywords to clipboard
python mcb.pyw del <keyword> - Deletes keyword from mcb
python mcb.pyw delall - Deltes all keywords from mcb
"""

import shelve, pyperclip, sys
def mcb():
    mcbshelf = shelve.open('mcb')

    # Save clipboard content
    if (len(sys.argv) == 3) and (sys.argv[1].lower() == "save"):
        mcbshelf[sys.argv[2]] = pyperclip.paste()
    # Delete a clipboard entry
    if (len(sys.argv) == 3) and (sys.argv[1].lower() == "del"):
        del mcbshelf[sys.argv[2]]
    elif len(sys.argv) == 2:
        # list the mcb items in the clipboard
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbshelf.keys())))
        # load an mcb item to the clipboard
        elif sys.argv[1] in mcbshelf:
            pyperclip.copy(mcbshelf[sys.argv[1]])
        # delete all entries
        if sys.argv[1].lower() == 'delall':
            mcbshelf.clear()

    mcbshelf.close()
mcb()
