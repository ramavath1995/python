from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# count.click()
# button = driver.find_element(By.NAME, value="search")
# button.send_keys("python", Keys.ENTER)
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://secure-retreat-92358.herokuapp.com/')

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("ramavath", Keys.TAB)
f_name = driver.find_element(By.NAME, value="lName")
f_name.send_keys("dhakya", Keys.TAB)
f_name = driver.find_element(By.NAME, value="email")
f_name.send_keys("dhakya31@gmail.com", Keys.ENTER)