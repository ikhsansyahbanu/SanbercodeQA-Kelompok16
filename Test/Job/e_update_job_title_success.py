import unittest
import time
from selenium import webdriver
from object.pageObject import PageObject
from a_job_titles_page import TestViewJobTitlesPage
import json

class TestUpdateJobTitlesSuccess(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)
        TestViewJobTitlesPage.test_verify_job_titles(self)

    def test_update_job_success(self):
        # Test Case ID: ADJT-008
        driver = self.browser

        with open('./data/data.json') as d:
            data = json.load(d)
        # 1. Click one of edit button (pen icon) in Action column
        PageObject.clickByXpath(self, "//div[@class='oxd-table-body']/div[1]/div/div[4]/div/button[2]")
        # 2. Input Job Description
        PageObject.inputByXpath(self, "//form[@class='oxd-form']/div[2]/div/div[2]/textarea", data["lorem"])
        # 3. Click Save button
        PageObject.clickByXpath(self, "//button[contains(.,' Save ')]")
        time.sleep(5)

        # Validation
        assert data["lorem"] in driver.page_source

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()