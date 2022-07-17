import requests
import os
from sys import platform
from bs4 import BeautifulSoup

get_link = input("Please enter your link from melovy.ir:\n ")

url = get_link
grab = requests.get(url)
soup = BeautifulSoup(grab.text, 'html.parser')
get_current_path = os.getcwd()
# opening a file in write mode
f = open("links.txt", "w")
# traverse paragraphs from soup
for link in soup.find_all("audio"):
    data = link.get('src')
    f.write(data)
    f.write("\n")
f.close()
os.system("wget -i links.txt")
