from tracemalloc import start
import requests
import os
from bs4 import BeautifulSoup
class main():
    def start():
        get_link = input("Please enter your link from melovy.ir:\n ")
        url = get_link
        grab = requests.get(url)
        soup = BeautifulSoup(grab.text, 'html.parser')
        f = open("links.txt", "w")
        for link in soup.find_all("audio"):
            data = link.get('src')
            f.write(data)
            f.write("\n")
        f.close()
        os.system("wget -i links.txt")
main.start()