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
web.get("https://timesprayer.com/prayer-times-cities-egypt.html")

prayer_times = []
css_selector = ["body > div.container > div.containerBlock.prayerBlock > div > div.prayerDes > div > div:nth-child(1) > table > tbody > tr.active", 
                "body > div.container > div.containerBlock.prayerBlock > div > div.prayerDes > div > div:nth-child(1) > table > tbody > tr:nth-child(2)", 
                "body > div.container > div.containerBlock.prayerBlock > div > div.prayerDes > div > div:nth-child(1) > table > tbody > tr:nth-child(3)", 
                "body > div.container > div.containerBlock.prayerBlock > div > div.prayerDes > div > div:nth-child(1) > table > tbody > tr:nth-child(4)", 
                "body > div.container > div.containerBlock.prayerBlock > div > div.prayerDes > div > div:nth-child(1) > table > tbody > tr:nth-child(5)", 
                "body > div.container > div.containerBlock.prayerBlock > div > div.prayerDes > div > div:nth-child(1) > table > tbody > tr:nth-child(6)"]

test = web.find_element(By.CSS_SELECTOR, "#q")
test.send_keys("El Dabaa", Keys.ARROW_DOWN)
web.find_element(By.CLASS_NAME, "search").click()
web.find_element(By.CSS_SELECTOR, "body > div.container > div.containerBlock > div.oneResult > a").click()

for i in range(len(css_selector)):
    prayer = web.find_element(By.CSS_SELECTOR, css_selector[i]).text
    prayer_times.append(prayer)
with open(r"E:\my project\py_projects\prayer_times.txt", "w", encoding="utf-8") as f:
    for prayer_time in prayer_times:
        f.write(prayer_time)
        f.write("\n\n")
f.close()
web.close()