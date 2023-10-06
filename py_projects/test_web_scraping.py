from import_selenium import *

def path ():
    file_path = input("enter the path: ").strip()
    if file_path == "":
        file_path = r"C:\Users\Public\Downloads\prayer_times.txt"
    else:
        file_path = file_path + r"\prayer_times.txt"
    return file_path
path_file = path()
user_input = input("enter your governorate: ").strip().capitalize()
prayer_times = []

web = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
web.get("https://timesprayer.com/prayer-times-cities-egypt.html")
test = web.find_element(By.CSS_SELECTOR, "#q")
test.send_keys(f"{user_input}", Keys.ARROW_DOWN)
web.find_element(By.CLASS_NAME, "search").click()
web.find_element(By.CSS_SELECTOR, "body > div.container > div.containerBlock > div.oneResult > a").click()
for i in range(1, 7):
    prayer = web.find_element(By.CSS_SELECTOR, f"body > div.container > div.containerBlock.prayerBlock > div > div.prayerDes > div > div:nth-child(1) > table > tbody > tr:nth-child({i})").text
    prayer_times.append(prayer)
with open(f"{path_file}", "w", encoding="utf-8") as f:
    for prayer_time in prayer_times:
        f.write(prayer_time)
        f.write("\n\n")

f.close()
web.close()
print(f"to open the file copy this path =>{path_file} and paste it in path search box.")