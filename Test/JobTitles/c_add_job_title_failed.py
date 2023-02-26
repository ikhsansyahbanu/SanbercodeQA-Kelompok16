import unittest
import time
from selenium import webdriver
from object.pageObject import PageObject
from a_job_titles_page import TestViewJobTitlesPage
import json
import os

class TestAddJobTitlesFailed(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)
        TestViewJobTitlesPage.test_verify_job_titles(self)

    def test_add_job_failed(self):
        driver = self.browser
        with open('./data/data.json') as d:
            data = json.load(d)

        PageObject.clickByXpath(self, "//button[contains(.,' Add ')]")
        # Test Case ID: ADJT-004 Job title field empty
        ## 1. Input Job Description
        PageObject.inputByXpath(self, "//form[@class='oxd-form']/div[2]/div/div[2]/textarea", data["desc"])
        ## 2. Input file in Job Specification field            
        PageObject.inputByXpath(self, "//input[@type='file']", os.getcwd() + data["fileLess1mb"])
        ## 3. Input Note
        PageObject.inputByXpath(self, "//form[@class='oxd-form']/div[4]/div/div[2]/textarea", data["note"])
        ## 4. Click Save button
        PageObject.clickByXpath(self, "//button[contains(.,' Save ')]")
        ### Validation
        PageObject.errorMessage(self, driver, 'Required')
        driver.refresh()
        time.sleep(5)

        # Test Case ID: ADJT-003 Input Job Title with data that already exist
        ## Input Job Title
        PageObject.inputByXpath(self, "//form[@class='oxd-form']/div[1]/div/div[2]/input", data["title"])
        ### Validation
        PageObject.errorMessage(self, driver, 'Already exists')
        driver.refresh()
        time.sleep(5)

        # Test Case ID: ADJT-005 Input Job Specification with size file > 1mb
        ## Input file in Job Specification
        PageObject.inputByXpath(self, "//input[@type='file']", os.getcwd() + data["fileMore1mb"])
        ### Validation
        PageObject.errorMessage(self, driver, 'Attachment Size Exceeded')

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()