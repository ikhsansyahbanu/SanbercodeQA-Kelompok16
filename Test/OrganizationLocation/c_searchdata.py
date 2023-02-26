import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class Testsearchdata(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_search_full(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #login button
        time.sleep(2) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() #menu admin
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() #organization button
        time.sleep(3) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() #Location button
        time.sleep(2) 

        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Aurora Anna shop") # isi name
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("macao") # isi city
        time.sleep(3)
        #dropdown country
        wait = WebDriverWait(driver,0)
        dropdown = wait.until(EC.visibility_of_element_located(
          (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]")))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(2)
        dropdown.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik search
        time.sleep(6)

    def test_b_search_blank_city_and_country(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #login button
        time.sleep(2) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() #menu admin
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() #organization button
        time.sleep(3) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() #Location button
        time.sleep(2) 

        #search by name
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Aurora Anna shop") # isi name
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik search
        time.sleep(6)

    def test_c_search_blank_name_and_country(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #login button
        time.sleep(2) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() #menu admin
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() #organization button
        time.sleep(3) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() #Location button
        time.sleep(2) 

        #search by city
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("macao") # isi city
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik search
        time.sleep(6)

    def test_d_search_blank_name_and_city(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #login button
        time.sleep(2) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() #menu admin
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() #organization button
        time.sleep(3) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() #Location button
        time.sleep(2) 

        #search by country
        wait = WebDriverWait(driver,0)
        dropdown = wait.until(EC.visibility_of_element_located(
          (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]")))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(2)
        dropdown.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click() # klik search
        time.sleep(6)
        
    def test_e_verify_reset_button(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #login button
        time.sleep(2) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click() #menu admin
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span").click() #organization button
        time.sleep(3) 
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a").click() #Location button
        time.sleep(2) 

        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Aurora Anna shop") # isi name
        time.sleep(3)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys("macao") # isi city
        time.sleep(3)
        #dropdown country
        wait = WebDriverWait(driver,0)
        dropdown = wait.until(EC.visibility_of_element_located(
          (By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]")))
        dropdown.click()
        dropdown.send_keys("random")
        time.sleep(2)
        dropdown.send_keys(Keys.RETURN)
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]").click() #reset button
        time.sleep(6)

def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()