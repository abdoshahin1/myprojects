from import_selenium import *

path_file = path()
user_input = input("enter your governorate: ").strip().capitalize()
prayer_times = []

web.get("https://timesprayer.com/prayer-times-cities-egypt.html")
test = web.find_element(By.CSS_SELECTOR, "#q")
test.send_keys(f"{user_input}", Keys.ARROW_DOWN)
web.find_element(By.CLASS_NAME, "search").click()
web.find_element(By.CSS_SELECTOR, "body > div.container > div.containerBlock > div.oneResult > a").click()
for i in range(1, 7):
    prayer = web.find_element(By.CSS_SELECTOR,
                              f"body > div.container > div.containerBlock.prayerBlock > div > div.prayerDes > div >"
                              f" div:nth-child(1) > table > tbody > tr:nth-child({i})").text
    prayer_times.append(prayer)
with open(f"{path_file}", "w", encoding="utf-8") as f:
    for prayer_time in prayer_times:
        f.write(prayer_time)
        f.write("\n\n")

f.close()
web.close()
print(f"to open the file copy this path =>{path_file} and paste it in path search box.")
