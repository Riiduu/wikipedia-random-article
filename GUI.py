from PyQt5.QtWidgets import *
from PyQt5 import uic

import requests
from bs4 import BeautifulSoup
import webbrowser

url = "url"
soup = "soup"
title = "title"

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("GUI.ui", self)
        self.show()

        self.pushButton_2.clicked.connect(self.generateUrl)
        
        self.pushButton.clicked.connect(self.openLink)

    

    def generateUrl():
        global url
        url = requests.get("https://en.wikipedia.org/wiki/Special:Random")

        return url

    def generateSoup():
        global soup
        soup = BeautifulSoup(url.content, "html.parser")

        return soup

    def generateTitle():
        global title
        title = soup.find(class_="firstHeading").text
        return title

    url = generateUrl()
    soup = generateSoup()
    title = generateTitle()
    


    # def generateLink(self):
    #     url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    #     soup = BeautifulSoup(url.content, "html.parser")
    #     # Update title value
    #     self.label.setText(soup.find(class_="firstHeading").text) 
        
    # def openLink():
    #     url = "https://en.wikipedia.org/wiki/%s" % title
    #     webbrowser.open(url)





def main():
    app = QApplication([])
    window = MainWindow()

    app.exec_()

if __name__ == "__main__":
    main()