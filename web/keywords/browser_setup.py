import configparser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BrowserSetup:
    @staticmethod
    def get_driver():
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy path driver từ phần cấu hình webdriver
        driver_path = config['webdriver']['driver_path']

        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(26)
        driver.maximize_window()
        return driver