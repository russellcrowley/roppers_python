#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
def roppers_login():
# get credentials (rather than save)
    username = input("Enter username: ")
    password = input("Enter password: ")
    payload = {"username":username, "password":password}
# access academy.hoppersroppers.org with credentials
    s = requests.Session()
    r = s.post("https://academy.hoppersroppers.org/login/index.php", data=payload)
# download everything linked to from computing fundamentals page
    cf = s.get("https://academy.hoppersroppers.org/course/view.php?id=8")
    soup = BeautifulSoup(cf.text, "html.parser")
    broken_links = []
    print("Here are the working links: ")
    for link in soup.find_all('a'):
        print(link.get('href'))
    
roppers_login()


    