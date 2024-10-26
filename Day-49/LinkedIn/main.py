import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

mail = "dhakya31@gmail.com"
e_password = "Dhakya@29"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3847493074&geoId=102713980&keywords=devops%20engineer&location=India&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")
time.sleep(2)
a = driver.find_element(By.LINK_TEXT, "Sign in")
a.click()

time.sleep(5)
email = driver.find_element(By.ID, "username")
email.send_keys(mail)
password = driver.find_element(By.ID, "password")
password.send_keys(e_password)
password.send_keys(Keys.ENTER)

time.sleep(5)
button = driver.find_element(By.ID, "#ember728 button")
button.click()
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()

num = "1234567890"
phone = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3847493074-115421157-phoneNumber-nationalNumber"]')
phone.send_keys(num)
phone.send_keys(Keys.ENTER)

next_ = driver.find_element(By.LINK_TEXT, "Next")
next_.click()