import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

url ='https://thbhrms.darwinbox.in/user/login'

class Testlogin( ):
    driver = None

    def __init__(self):
        self.get_count = None

    @classmethod
    def test_setup(self, url):
        chrome_options = webdriver.ChromeOptions( )
        prefs = {"profile.default_content_setting_values.notifications": 1}
        chrome_options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(2)
        self.driver.maximize_window( )
        self.driver.get(url)
        time.sleep(2)
        return self.driver

    def test_login(self, username, password):  ## Login Functionality
        # __doc__="Test discription"
        driver = self.driver
        time.sleep(5)
        driver.find_element(By.ID, "UserLogin_username").click( )
        driver.find_element(By.ID, "UserLogin_username").send_keys(username)
        time.sleep(3)
        driver.find_element(By.ID, "UserLogin_password").click( )
        driver.find_element(By.ID, "UserLogin_password").send_keys(password)
        time.sleep(3)
        driver.find_element(By.ID, "login-submit").click( )


class attendance():
    def clock_in(self):
        driver = Testlogin().driver
        driver.find_element(By.XPATH,"/html/body/div[2]/div/nav/div[1]/div/div[8]/div").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//ul[@class='list-inline display-inline-flex align-items-center']//a[@id='attendance-logger-widget']").click()
        time.sleep(10)
        driver.close()


    def clock_out(self):
        driver = Testlogin( ).driver
        driver.find_element(By.XPATH, "/html/body/div[2]/div/nav/div[1]/div/div[8]/div").click( )
        time.sleep(5)
        driver.find_element(By.XPATH,
                            "//ul[@class='list-inline display-inline-flex align-items-center']//a[@id='attendance-logger-widget']").click( )
        time.sleep(10)
        driver.close( )