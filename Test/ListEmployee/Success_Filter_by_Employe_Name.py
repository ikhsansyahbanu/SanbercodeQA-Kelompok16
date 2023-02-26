import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from object.pageObject import PageObject

class TestFilterByEmployeeName(unittest.TestCase):
    # Test Case ID: TC02
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)

    def test_filter_by_employee_name (self):
        driver = self.browser
        # 1. Click PIM menu
        PageObject.clickByXpath(self, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
        # 2. Click Employee List
        PageObject.clickByXpath(self, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
        # 3. Fill Field 
        PageObject.inputByXpath(self, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div/input", "Cassidy  Hope")
        # 4. Click Search
        PageObject.clickByXpath(self, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
        
        # Validation 
        title = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[8]/div")
        print(title)
        self.assertIn('Cassidy  Hope', title)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()