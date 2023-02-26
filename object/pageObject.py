import unittest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PageObject(unittest.TestCase):

    def getBaseUrl(self, driver):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(1)

    def inputByName(self, name, keys):
        driver = self.browser
        driver.find_element(By.NAME, name).send_keys(keys)
        time.sleep(1)

    def inputByXpath(self, xpath, keys):
        driver = self.browser
        driver.find_element(By.XPATH, xpath).send_keys(keys)
        time.sleep(1)

    def clickByXpath(self, xpath):
        driver = self.browser
        driver.find_element(By.XPATH, xpath).click()
        time.sleep(2)

    def clickByCss(self, css_selector):
        driver = self.browser
        driver.find_element(By.CSS_SELECTOR, css_selector).click()
        time.sleep(2)

    def clickByLinkText(self, text):
        driver = self.browser
        driver.find_element(By.LINK_TEXT, text).click()
        time.sleep(2)

    def login(self, driver):
        PageObject.getBaseUrl(self, driver)
        PageObject.inputByName(self, "username", "Admin")
        PageObject.inputByName(self, "password", "admin123")
        PageObject.clickByXpath(self, "//button[@type='submit']")

    def errorMessage(self, driver, msg):
        error = driver.find_element(By.CSS_SELECTOR, "span.oxd-input-field-error-message").text
        self.assertIn(msg, error)
        time.sleep(2)

    def check_exists_by_xpath(driver, xpath):
        try:
            driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True