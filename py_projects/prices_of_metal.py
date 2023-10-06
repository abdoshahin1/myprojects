from import_selenium import *

# file_path = path()
prices_list = []

web.get("https://google.com/")
web.find_element(By.CSS_SELECTOR, "#APjFqb").send_keys("مصر اليوم", Keys.ARROW_DOWN)
web.find_element(By.CSS_SELECTOR, "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.FPdoLc.lJ9FBc > center > input.gNO89b").click()
web.find_element(By.CSS_SELECTOR, "#rso > div.hlcw0c > div > div > div > div > div > div > div > div.yuRUbf > div > span > a > h3").click()
web.find_element(By.CSS_SELECTOR, "body > div:nth-child(4) > header > div.large-9.columns > div.search_wrap > form > input[type=text]:nth-child(1)").send_keys("سعر الحديد اليوم", Keys.ARROW_DOWN)
web.find_element(By.CSS_SELECTOR, "body > div:nth-child(4) > header > div.large-9.columns > div.search_wrap > form > input.search_icon").click()
web.find_element(By.CSS_SELECTOR, "body > div:nth-child(15) > div.large-8.columns.advancedSearch > div:nth-child(4) > ul > li:nth-child(1)").click()
# to get the title of metal article
title = web.find_element(By.CSS_SELECTOR, "#NewsStory > h2:nth-child(13)").text
prices_list.append(title)
# to get the contact of metal article
for i in range(16, 25, 3):
    prices_list.append(web.find_element(By.CSS_SELECTOR, f"#NewsStory > p:nth-child({i})").text)
# to get the title of cement article
title1 = web.find_element(By.CSS_SELECTOR, "#NewsStory > h2:nth-child(52)").text
prices_list.append(title1)
for j in range(55, 104, 24):
    if j == 103:
        prices_list.append(web.find_element(By.CSS_SELECTOR, f"#NewsStory > p:nth-child({j - 6})").text)
    else:
        prices_list.append(web.find_element(By.CSS_SELECTOR, f"#NewsStory > p:nth-child({j})").text)

# print the texts in file
with open(r"C:\Users\Public\Downloads\price_metal.txt", "w", encoding="utf-8") as f:
    for h in prices_list:
        f.write(h)
        f.write("\n\n")

f.close()
web.close()