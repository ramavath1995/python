from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

form_link = ("https://docs.google.com/forms/d/e/1FAIpQLSf3nd41u3Sj1VFSAkIbt5DkVjlR0A55i0_LcxMJnkjgGPzSRw/viewform?usp"
             "=sf_link")
zillow_link = "https://appbrewery.github.io/Zillow-Clone/"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=zillow_link, headers=head)
result = response.text

soup = BeautifulSoup(result, "html.parser")
link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in link_elements]
print(all_links)

address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_address = [address.getText().replace("|", "").strip() for address in address_elements]
print(all_address)

price_elements = soup.select(".PropertyCardWrapper span")
all_prices = [price.getText().split("+")[0] for price in price_elements]
print(all_prices)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(all_links)):
    driver.get(form_link)
    sleep(2)
    address = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div['
                                  '1]/input')
    address.send_keys(all_address[i])
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(all_links[i])
    price = driver.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(all_prices[i])
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()
