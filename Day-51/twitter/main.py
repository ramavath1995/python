from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


UPLOAD = 10
DOWNLOAD = 150
TWITTER_MAIL = 'dhakya1995@gmail.com'
TWITTER_PASS = "Dhakya@29"
# CHROME_PATH = "C:\Users\dhaky\.cache\selenium\chromedriver\win64\123.0.6312.105\chromedriver.exe"



class InternetSpeed:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.UP = 0
        self.Down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        con = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        con.click()
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(60)
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.UP = up_speed.text
        down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.Down = down_speed.text
        print(f"UP = {self.UP}")
        print(f"DOwn = {self.Down}")
    def tweet_to_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
        time.sleep(5)
        email.send_keys(TWITTER_MAIL)


bot = InternetSpeed()
bot.get_internet_speed()
bot.tweet_to_provider()

#react-root > div > div > div > main > div > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox > div.css-175oi2r.r-16y2uox.r-1jgb5lz.r-13qz1uu > div > div.css-175oi2r.r-1f1sjgu.r-mk0yit.r-13qz1uu > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input