#!/usr/bin/env python3
"""
Write a program that goes to a photo-sharing site like Flickr or Imgur, 
searches for a category of photos, and then downloads all the resulting images. 
You could write a program that works with any photo site that has a search feature.
"""

import requests
from bs4 import BeautifulSoup
import os
def image_downloader(search_term=None, pics=None):
    if search_term == None:
        search_term = input("Enter your search term: ")
    if pics == None:
        pics = int(input("How many pictures do you want? "))
    # Get pages results and a list of image urls
    r = requests.get(f"https://imgur.com/search?q={search_term}")
    soup = BeautifulSoup(r.text, "html.parser")
    images = []
    for link in soup.find_all("img"):
        image = (link.get('src'))
        # Remove 'b' from thumbnail link to get high quality image
        if image.startswith("//i.imgur.com/"):
            images.append(f"https:{image[0:-5]}.jpg")
        else:
            pass
    # Make directory named after search term
    os.mkdir(search_term)
    # Don't index beyond amount of images
    if len(images) < pics:
        pics = len(images)
    # Get image and save in directory

    for i in range(pics):
        print(f"Saving {images[i]}...")
        image_file = open(os.path.join(search_term, os.path.basename(images[i])), 'wb')
        image = requests.get(images[i])
        for chunk in image.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
    print(f"All done! Saved {pics} images in a {search_term} folder in your current directory.")

image_downloader()

"""
-Messed about with the site format, chose imugr because it looked a bit easier
-Found a way to access high quality image through changing thumbnail, impressed myself!
-Copie ATBS a bit when writing images

TODO:
-Sort out argv values to run
-Prevent directory being overwritten
-Do this with an API
-Do this for flickr
-Parse image name using regex
"""