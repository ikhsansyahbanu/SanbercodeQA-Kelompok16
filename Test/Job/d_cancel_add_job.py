import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from object.pageObject import PageObject
from a_job_titles_page import TestViewJobTitlesPage

class TestCancelAddJobTitles(unittest.TestCase):
    # Test Case ID: ADJT-006
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)
        TestViewJobTitlesPage.test_verify_job_titles(self)

    def test_add_job_success(self):
        # 1. Click + Add button
        PageObject.clickByXpath(self, "//button[contains(.,' Add ')]")
        # 2. Input Job Title
        PageObject.clickByXpath(self, "//button[contains(.,' Cancel ')]")

        # Validation
        driver = self.browser
        title = driver.find_element(By.CSS_SELECTOR, "h6.orangehrm-main-title").text
        self.assertIn('Job Titles', title)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()