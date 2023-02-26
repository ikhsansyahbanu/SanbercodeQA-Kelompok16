import unittest
import time
from selenium import webdriver
from object.pageObject import PageObject
from a_job_titles_page import TestViewJobTitlesPage
from selenium.webdriver.common.by import By

class TestDeleteJobSuccess(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        PageObject.login(self, self.browser)
        TestViewJobTitlesPage.test_verify_job_titles(self)

    def test_delete_job_success(self):
        # Test Case ID: ADJT-011
        driver = self.browser
        textBefore_1 = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[2]/div").text
        # 1. Click one of delete button (trash icon) in Action column
        PageObject.clickByXpath(self, "//div[@class='oxd-table-body']/div[1]/div/div[4]/div/button[1]")
        # # 2. Confirmation modal appears
        checkpoint = driver.find_element(By.XPATH, "//div[@role='dialog']//p[contains(., 'Are you Sure?')]").text
        self.assertIn('Are you Sure?', checkpoint)
        # 3. Click Yes, Delete button in modal 
        PageObject.clickByXpath(self, "//button[contains(.,' Yes, Delete ')]")

        # Validation
        time.sleep(3)
        textAfter_1 = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']/div[1]/div/div[2]/div").text
        self.assertIsNot(textBefore_1, textAfter_1)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()