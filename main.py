from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LINK = "https://forms.gle/QhXDVSQdxpnm9JbLA"

# ------------------------------------- BeautifulSoup -----------------------------------------

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.text)

link_list = []
price_list = []
location_list = []

links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
for link in links:
    href = link.get("href")
    link_list.append(href)
# print(link_list)

prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
for price in prices:
    formated_text = (price.getText().replace("+/mo", "")
                     .replace("+ 1 bd", "")
                     .replace("/mo", "")
                     .replace("+ 1bd", ""))
    price_list.append(formated_text)
# print(price_list)

locations = soup.find_all(name="address")
for location in locations:
    text = location.getText().strip()
    location_list.append(text)
# print(location_list)

# ------------------------------------- Selenium -----------------------------------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(0, len(links) - 1):
    driver.get(FORM_LINK)
    f_address = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
                                                    '/div/div/div[2]/div/div[1]/div/div[1]/input')
    f_price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div'
                                                  '[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    f_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]'
                                                 '/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(1)
    f_address.send_keys(location_list[i])
    f_price.send_keys(price_list[i])
    f_link.send_keys(link_list[i])

    submit = driver.find_element(By.CLASS_NAME, value="QvWxOd")
    submit.click()
