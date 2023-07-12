import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Bora\\AppData\\Local\\Google\\Chrome\\User Data")
chromedriver_path = "path_to_chromedriver"  # Replace with the actual path to chromedriver.exe
driver = webdriver.Chrome()

driver.get("https://stntrading.eu/buy/stranges/15")

element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, '//input[@class="btn_green_white_innerfade" and @value="Oturum Aç"]'))
)

element.click()
for i in range(5):
    print(i + 1)
    time.sleep(1)
the_html = driver.page_source
soup = BeautifulSoup(the_html, 'html.parser')
def checkPrices(name_info,paint_info):

    base_url = "https://backpack.tf/api/classifieds/listings/snapshot"

    api = "6484bdc2d83b49227d01d093"
    token = "9sUT4ydeVfMUKCj7C0Q/TgYIJLN6xgFh/nyJym4GxNE="
    appid = "440"
    sku = name_info

    urlF = base_url + "?token=" + token + "&api" + api + "&appid=440&sku=" + sku

    response = requests.get(urlF)

    if response.status_code == 200:
        print(name_info," ",price_info," ",paint_info)
        for i in response.json()["listings"]:
            if i["intent"] == "sell":
                continue
            print(i["intent"], " ", i["currencies"])
        print("---------------------------------------------------------")
    else:
        print("Error:", response.status_code)

img_elements = soup.find_all('img', class_='position-relative')
driver.quit()

for img in img_elements:
    # Get the aria-label attribute value of the img element
    aria_label = img.get('aria-label')
    soup_aria_label = BeautifulSoup(aria_label, 'html.parser')
    price_info = soup_aria_label.find('div', class_='inventoryItem-Price').text.strip()
    name_info = soup_aria_label.find('div', class_='inventoryItem-Tooltip-ItemName').text.strip()
    try:
        paint_info = soup_aria_label.find('div', class_='inventoryItem-Paint').text.strip()
    except:
        continue
    """print("Name: " + f"{name_info : <40}", end=" ")
    print(f"{paint_info: <45}", " ", price_info)"""

    checkPrices(name_info,paint_info)


