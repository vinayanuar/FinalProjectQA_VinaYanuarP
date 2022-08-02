import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_Login_Negatif(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") 
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("ihvi") 
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("ihvi010122") 
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()

unittest.main()