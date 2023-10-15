import requests
from bs4 import BeautifulSoup
import csv
# get the date from the user 
date = int(input("Enter the date that you want :").strip())
# get the url of the website
browser = requests.get(f"")

src = browser.content

soup = BeautifulSoup(src, "lxml")

test = soup.c
