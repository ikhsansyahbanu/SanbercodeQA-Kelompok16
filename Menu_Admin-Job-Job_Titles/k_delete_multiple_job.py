import unittest
import time
from selenium import webdriver
from object.pageObject import PageObject
from a_job_titles_page import TestViewJobTitlesPage
from selenium.webdriver.common.by import By

class TestDeleteMultipleJob(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)
        TestViewJobTitlesPage.test_verify_job_titles(self)

    def test_delete_multiple_job(self):
        # Test Case ID: ADJT-013 Verify Delete Multiple Job Titles Success
        driver = self.browser    
        textBefore_1 = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[2]/div").text
        textBefore_2 = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[2]/div/div[2]/div").text
        # 1. Click checkbox in two job titles
        PageObject.clickByXpath(self, "//div[@class='oxd-table-body']/div[1]//div[@class='oxd-checkbox-wrapper']")
        PageObject.clickByXpath(self, "//div[@class='oxd-table-body']/div[2]//div[@class='oxd-checkbox-wrapper']")
        # 2. Click Delete Selected Button
        PageObject.clickByXpath(self, "//button[contains(., 'Delete Selected')]")
        # 3. Confirmation modal appears 
        checkpoint = driver.find_element(By.XPATH, "//div[@role='dialog']//p[contains(., 'Are you Sure?')]").text
        self.assertIn('Are you Sure?', checkpoint)
        # 4. Click Yes, Delete button in modal 
        PageObject.clickByXpath(self, "//button[contains(.,' Yes, Delete ')]")

        # Validation
        textAfter_1 = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[2]/div").text
        textAfter_2 = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[2]/div/div[2]/div").text
        self.assertNotIn(textBefore_1, textAfter_1)
        self.assertNotIn(textBefore_2, textAfter_2)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()