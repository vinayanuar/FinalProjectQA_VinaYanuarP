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
    def test_Login_Positif(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys("Admin") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()

        response_message = driver.find_element(By.ID,"menu_recruitment_viewRecruitment").text
        self.assertEqual(response_message, 'Recruitment')

    def test_Job(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"menu_pim_viewPimModule").click()
        driver.find_element(By.ID,"menu_recruitment_viewCandidates").click()
        driver.find_element(By.ID,"candidateSearch_candidateName").click()
        time.sleep(3)
        driver.find_element(By.ID,"btnSrch").click()
        time.sleep(3)
        driver.find_element(By.ID,"candidateSearch_candidateNamed").send_keys("Archie Augustine")

unittest.main()