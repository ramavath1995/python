from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/events/python-events/")

# o=driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div/div/ul/li[1]/p/time')
date = driver.find_elements(By.CSS_SELECTOR, value=".list-recent-events time")
name = driver.find_elements(By.CSS_SELECTOR, value=".list-recent-events li a")
dates = [time.text for time in date]
names = [n.text for n in name]
events = {}
# event_dict = {key: value for (key, value) in zip(dates, names)}
for n in range(len(dates)):
    events[n + 1] = {
        "date": dates[n],
        "name": names[n],
    }
print(events)
driver.close()
