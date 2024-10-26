from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# FB_EMAIL = YOUR FACEBOOK LOGIN EMAIL
# FB_PASSWORD = YOUR FACEBOOK PASSWORD
co = webdriver.ChromeOptions()
co.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=co)

driver.get("http://www.tinder.com")

sleep(5)
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

#Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
# email.send_keys(FB_EMAIL)
# password.send_keys(FB_PASSWORD)
# password.send_keys(Keys.ENTER)
#
# #Switch back to Tinder window
# driver.switch_to.window(base_window)
# print(driver.title)