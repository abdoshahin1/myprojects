import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

browser = requests.get("https://timesprayer.com/prayer-times-cities-egypt.html")

src = browser.content

soup = BeautifulSoup(src, "lxml")

test = soup.find_all("input", {"type": "search"})
