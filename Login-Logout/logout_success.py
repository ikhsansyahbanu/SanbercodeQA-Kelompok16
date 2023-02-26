import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogoutSuccess(unittest.TestCase):
    # Test Case ID: LOG-005
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        driver = self.browser
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

    def test_logout_success(self):
        driver = self.browser
        time.sleep(2)
        # Login
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

        # 1. Click Profile
        driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        time.sleep(1)
        # 2. Click Logout
        driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']/li[4]").click()
        time.sleep(2)        
        
        # Validation 
        title = driver.find_element(By.CSS_SELECTOR, "h5.orangehrm-login-title").text
        self.assertIn('Login', title)
        time.sleep(1)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()