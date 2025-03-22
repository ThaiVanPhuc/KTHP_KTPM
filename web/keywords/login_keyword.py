from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.menu_login = (By.XPATH,"//a[contains(text(),'Đăng nhập')]")
        self.username_input = (By.XPATH, "//input[@id='email']") 
        self.password_input = (By.XPATH, "//input[@id='password']") 
        self.login_button = (By.XPATH, "//button[contains(text(),'Đăng nhập')]") 
        self.error_messeges = (By.XPATH,"//div[@class='user-message-error']")
        
    def open_login_page(self):
        self.driver.find_element(*self.menu_login).click()
    def enter_username(self,username):
        self.driver.find_element(*self.username_input).send_keys(username)
    def enter_password(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)
    def click_login_btn(self):
        self.driver.find_element(*self.login_button).click()
    def verify_error_login(self):
        self.driver.find_element(*self.error_messeges)