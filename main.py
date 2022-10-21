import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    print(f"{title} \n Do you want to view it? (y/n) ", end="")
    answer = input().lower()

    if answer == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url) # Opens url in default web browser
        break
    elif answer == "n":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break