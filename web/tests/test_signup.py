import unittest
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# File Excel lưu tài khoản
EXCEL_FILE = "users.xlsx"

class SignupTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Khởi tạo trình duyệt Chrome
        cls.driver.get("https://example.com/signup")  # Thay URL bằng trang signup của bạn
        cls.driver.maximize_window()

    def test_signup(self):
        """TC_01: Đăng ký tài khoản mới và lưu vào Excel"""
        driver = self.driver

        # Tạo email và password ngẫu nhiên
        new_email = f"user{int(time.time())}@gmail.com"
        new_password = "Test@1234"

        # Nhập thông tin đăng ký
        driver.find_element(By.NAME, "email").send_keys(new_email)
        driver.find_element(By.NAME, "password").send_keys(new_password)
        driver.find_element(By.NAME, "confirm_password").send_keys(new_password)
        driver.find_element(By.ID, "signup_button").click()
        time.sleep(3)  # Chờ trang load

        # Kiểm tra đăng ký thành công
        success_message = driver.find_element(By.ID, "success_message").text
        self.assertIn("Đăng ký thành công", success_message)

        # Ghi dữ liệu vào Excel
        self.save_to_excel(new_email, new_password)
        print(f"✅ Đã đăng ký: {new_email} - {new_password}")

    def save_to_excel(self, email, password):
        """Lưu email & password vào file Excel"""
        try:
            wb = openpyxl.load_workbook(EXCEL_FILE)
            sheet = wb.active
        except FileNotFoundError:
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.append(["Email", "Password"])  # Tiêu đề nếu file chưa tồn tại

        sheet.append([email, password])  # Thêm dòng mới
        wb.save(EXCEL_FILE)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Đóng trình duyệt khi kết thúc test

if __name__ == "__main__":
    unittest.main()
