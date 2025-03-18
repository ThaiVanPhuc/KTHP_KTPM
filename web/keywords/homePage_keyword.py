from selenium.webdriver.common.by import By
from resources.locators.homePage_locator import HomePage_Locator

class HomePage:
    def __init__(self,driver):
        self.driver = driver
    def verify_logo_profile_visible(self):
        self.driver.find_element("xpath",HomePage_Locator.LOGO_PROFILE)
