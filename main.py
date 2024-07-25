from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_LINK = "https://forms.gle/QhXDVSQdxpnm9JbLA"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.text)

