#!/usr/bin/env python3
"""
Write a program that takes an email address and string of text 
on the command line and then, using selenium, logs in to your 
email account and sends an email of the string to the provided address. 
(You might want to set up a separate email account for this program.)
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def emailer(recipient=None, message=None):
    if recipient == None:
        recipient = input("Email address: ")
    if message == None:
        message = input("Message to send: ")
    password = input("Password: ")
    #log in
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    browser.get("https://mail.protonmail.com/login")
    user_elem = browser.find_element_by_id("username")
    user_elem.send_keys("russ_python")
    password_elem = browser.find_element_by_id("password")
    password_elem.send_keys(password)
    #sleep to allow form to be submitted properly
    time.sleep(0.5)
    password_elem.submit()
    #click compose
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector('.compose').click()
    #enter recipient and subject
    time.sleep(1)
    recipient_elem = browser.find_element_by_name('autocomplete')
    recipient_elem.send_keys(recipient)
    #switch to subject
    browser.implicitly_wait(10)
    subject_elem = browser.find_element_by_xpath('/html/body/div[2]/form[1]/div/div[2]/div[5]/input')
    subject_elem.send_keys("Automated email from Russ!")
    #switch to iframe that has message body and submit message
    browser.implicitly_wait(10)
    frame = browser.find_element_by_class_name('squireIframe')
    browser.switch_to.frame(frame)
    message_elem = browser.find_element_by_tag_name('body')
    message_elem.send_keys(message)
    #switch back to main frame and send
    browser.switch_to.parent_frame()
    browser.implicitly_wait(10)
    send_elem = browser.find_element_by_css_selector("button.mobileFull:nth-child(4)").click()
    #finish up!
    time.sleep(2)
    browser.quit()
    print("Email sent!")


emailer()

"""
-Had to think about importing time to sleep so a form isn't submitted too early
-Found how to copy CSS elements and XPath after being stuck for ages!
-Protonmail seems tricky, had to look into iframes and all sorts!
TODO:
-Need to look into environment variables
-Headless browsers
-Different email clients

"""