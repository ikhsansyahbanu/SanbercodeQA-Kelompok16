import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from object.pageObject import PageObject

class TestFilterBySupervisorName(unittest.TestCase):
    # Test Case ID: TC03
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)

    def test_filter_by_supervisor_name (self):
        driver = self.browser
        PageObject.clickByXpath(self, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a")
        PageObject.clickByXpath(self, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a")
        PageObject.inputByXpath(self, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input", "Jordan")
        PageObject.clickByXpath(self, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
        
        # Validation 
        title = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div")
        self.assertIn('Jordan', title)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()