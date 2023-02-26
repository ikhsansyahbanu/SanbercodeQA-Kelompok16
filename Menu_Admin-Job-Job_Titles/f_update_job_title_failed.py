import unittest
import time
from selenium import webdriver
from object.pageObject import PageObject
from a_job_titles_page import TestViewJobTitlesPage
import json
import os

class TestUpdateJobTitlesFailed(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)
        TestViewJobTitlesPage.test_verify_job_titles(self)

    def test_update_job_failed(self):
        # Test Case ID: ADJT-010 Update Job Specification with size file > 1mb
        driver = self.browser

        with open('./data/data.json') as d:
            data = json.load(d)
        # 1. Click one of edit button (pen icon) in Action column
        PageObject.clickByXpath(self, "//div[@class='oxd-table-body']/div[1]/div/div[4]/div/button[2]")
        time.sleep(3)
        # 2. Click radio input Replace Current
        isExist = PageObject.check_exists_by_xpath(driver, "//input[@value='replaceCurrent']")
        if isExist == True:
            PageObject.clickByXpath(self, "//div[@class='orangehrm-file-options']/div[3]/div[2]/div/label/span")            
        # 3. Input file in Upload Job Specification
        PageObject.inputByXpath(self, "//input[@type='file']", os.getcwd() + data["fileMore1mb"])
        # Validation
        PageObject.errorMessage(self, driver, 'Attachment Size Exceeded')

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()