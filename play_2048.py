#!/usr/bin/env python3
"""
2048 is a simple game where you combine tiles by sliding them up, down, 
left, or right with the arrow keys. You can actually get a fairly high score 
by repeatedly sliding in an up, right, down, and left pattern over 
and over again. Write a program that will open the game at 
https://gabrielecirulli.github.io/2048/ and keep sending up, right, down, 
and left keystrokes to automatically play the game.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def play_2048():
    #load up browser
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get("https://gabrielecirulli.github.io/2048/")
    browser.implicitly_wait(10)
    print("Press CTRL + C to finish!")
    html_elem = browser.find_element_by_tag_name("html")
    # send key combos
    while True:
        browser.implicitly_wait(1)
        html_elem.send_keys(Keys.UP)
        browser.implicitly_wait(1)
        html_elem.send_keys(Keys.RIGHT)
        browser.implicitly_wait(1)
        html_elem.send_keys(Keys.DOWN)
        browser.implicitly_wait(1)
        html_elem.send_keys(Keys.LEFT)
    
play_2048()

"""
-This one was really quick!
Possible TODO:
-Prompt to click button to play again
-Record score on screen/in file
"""