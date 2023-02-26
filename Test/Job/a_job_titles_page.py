import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from object.pageObject import PageObject

class TestViewJobTitlesPage(unittest.TestCase):
    # Test Case ID: ADJT-001
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)

    def test_verify_job_titles (self):
        driver = self.browser
        # 1. Click Admin menu
        PageObject.clickByXpath(self, "//div[@class='oxd-sidepanel-body']/ul/li[1]/a//span[contains(.,'Admin')]")
        # 2. Click Job dropdown
        PageObject.clickByXpath(self, "//div[@class='oxd-topbar-body']/nav/ul/li[2]/span")
        # 3. Click Job Titles
        PageObject.clickByXpath(self, "//div[@class='oxd-topbar-body']/nav/ul/li[2]/ul/li[1]/a[contains(.,'Job Titles')]")
        
        # Validation 
        title = driver.find_element(By.CSS_SELECTOR, "h6.orangehrm-main-title").text
        self.assertIn('Job Titles', title)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()