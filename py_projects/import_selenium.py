from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
web = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

def path ():
    file_path = input("enter the path: ").strip()
    if file_path == "":
        file_path = r"C:\Users\Public\Downloads\prayer_times.txt"
    else:
        file_path = file_path + r"\prayer_times.txt"
    return file_path
