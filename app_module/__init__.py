from flask import Flask
from bs4 import BeautifulSoup

from urllib.request import urlopen

app = Flask(__name__)
trans = {}

url = 'https://studynow.ru/dicta/allwords'
req_page = urlopen(url)
html_page = req_page.read()
req_page.close()

soup = BeautifulSoup(html_page, 'html.parser')

items = soup.find_all('tr')

for i in items:
    j = i.find_all('td')
    k = j[1].text
    trans[k] = j[2].text

from app_module import routes