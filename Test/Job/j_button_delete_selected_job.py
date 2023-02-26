import unittest
from selenium import webdriver
from object.pageObject import PageObject
from a_job_titles_page import TestViewJobTitlesPage
from selenium.webdriver.common.by import By

class TestButtonDeleteSelected(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)
        TestViewJobTitlesPage.test_verify_job_titles(self)

    def test_button_delete_selected(self):
        # Test Case ID: ADJT-015 Verify Delete Selected Button appears when checkbox checked
        driver = self.browser
        # 1. Click checkbox in two job titles
        PageObject.clickByXpath(self, "//div[@class='oxd-table-body']/div[1]//div[@class='oxd-checkbox-wrapper']")
        PageObject.clickByXpath(self, "//div[@class='oxd-table-body']/div[2]//div[@class='oxd-checkbox-wrapper']")

        # Validation
        driver.find_element(By.XPATH, "//button[contains(., 'Delete Selected')]").is_displayed()

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()