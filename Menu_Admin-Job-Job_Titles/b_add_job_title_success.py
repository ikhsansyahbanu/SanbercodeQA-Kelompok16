import unittest
import time
from selenium import webdriver
from object.pageObject import PageObject
from a_job_titles_page import TestViewJobTitlesPage
import json
import os
import random  
import string  

class TestAddJobTitlesSuccess(unittest.TestCase):
    # Test Case ID: ADJT-002
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)
        TestViewJobTitlesPage.test_verify_job_titles(self)

    def test_add_job_success(self):
        with open('./data/data.json') as d:
            data = json.load(d)
        # 1. Click + Add button
        PageObject.clickByXpath(self, "//button[contains(.,' Add ')]")
        # 2. Input Job Title
        # job_title = ''.join((random.choice('abcdefghijk')) for x in range(5))
        PageObject.inputByXpath(self, "//form[@class='oxd-form']/div[1]/div/div[2]/input", data["title"])
        # 3. Input Job Description
        PageObject.inputByXpath(self, "//form[@class='oxd-form']/div[2]/div/div[2]/textarea", data["desc"])
        # 4. Input file in Job Specification field            
        PageObject.inputByXpath(self, "//input[@type='file']", os.getcwd() + data["fileLess1mb"])
        # 5. Input Note
        PageObject.inputByXpath(self, "//form[@class='oxd-form']/div[4]/div/div[2]/textarea", data["note"])
        # 6. Click Save button
        PageObject.clickByXpath(self, "//button[contains(.,' Save ')]")
        time.sleep(5)

        # Validation
        driver = self.browser
        assert data["title"] in driver.page_source

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()