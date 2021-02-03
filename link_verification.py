#!/usr/bin/env python3
"""
Write a program that, given the URL of a web page, will attempt to 
download every linked page on the page. The program should flag any 
pages that have a 404 “Not Found” status code and print them out as broken links.
"""
from bs4 import BeautifulSoup
import requests
import sys
def link_verification():
    # either get url from command line, else input
    if len(sys.argv) == 1:
        url = input("Enter a url to get links from: ")
    else:
        url = sys.argv[1]
    # scrape page
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    broken_links = []
    print("Here are the working links: ")
    for link in soup.find_all('a'):
        l = link.get('href')
        try:
            # print working links
            requests.get(l).raise_for_status()
            print(l)
        except Exception:
            broken_links.append(l)
    print("Broken links are: ")
    for i in broken_links:
        print(i)

link_verification()
"""
This was really quick as well!

Possible TODO:
-Save links to a txt doc (although I could do this through bash)
"""