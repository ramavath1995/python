from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

username = "9493638582"
password = "Dhakya@123"
account = "dr_brain138"
class InstagramFollowers:
    def __init__(self):

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")

        sleep(5)
        email = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        email.send_keys(username)
        password_ = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_.send_keys(password)
        sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        login_button.click()
        sleep(3.1)
        login_popups = self.driver.find_element(By.XPATH, '// div[contains(text(), "Not now")]')
        login_popups.click()
        sleep(3)
        notification_popups = self.driver.find_element(By.XPATH, '// button[contains(text(), "Not Now")]')
        notification_popups.click()

    def find_followers(self):
        sleep(2)
        self.driver.get(f"https://www.instagram.com/{account}/followers")
        sleep(6)
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                sleep(2)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


insta_bot = InstagramFollowers()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()

