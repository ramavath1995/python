from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com")
time.sleep(3)
accept = driver.find_element(By.XPATH, "//*[@id='q1887506695']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div")
accept.click()
time.sleep(5)
login_button = driver.find_element(By.LINK_TEXT, 'Log in')
login_button.click()
time.sleep(2)

base_window = driver.window_handles[0]
gmail_window = driver.window_handles[1]
driver.switch_to.window(gmail_window)
print(driver.title)

time.sleep(5)
google = driver.find_element(By.XPATH, '//*[@id="button-label"]')
google.click()


# //*[@id="container"]/div/div[2]/span[1]