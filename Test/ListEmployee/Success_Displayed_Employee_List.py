import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from object.pageObject import PageObject

class TestDisplayEmployeeList(unittest.TestCase):
    # Test Case ID: TC01
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)

    def test_display_employee_list (self):
        driver = self.browser
        PageObject.clickByXpath(self, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
        PageObject.clickByXpath(self, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
        
        # Validation 
        title = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span")
        self.assertIn('Records Found', title)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()