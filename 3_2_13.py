from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
     link = "http://suninjuly.github.io/registration1.html"
     browser = webdriver.Chrome()
     browser.get(link)
    
     input1 = browser.find_element(By.CSS_SELECTOR, "input.first")
     input1.send_keys("Ivan")
     input2 = browser.find_element(By.CSS_SELECTOR, "[class='form-control second'][required]" )
     input2.send_keys("Petrov")
     input3 = browser.find_element(By.CSS_SELECTOR, "input.third")
     input3.send_keys("m@test.ru")
     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
     button.click()
     
     time.sleep(2)  
     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1") 
     welcome_text = welcome_text_elt.text  

     self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "No Test")
     
    def test_abs2(self):
     link = "http://suninjuly.github.io/registration2.html"
     browser = webdriver.Chrome()
     browser.get(link)
    
     input1 = browser.find_element(By.CSS_SELECTOR, "input.first")
     input1.send_keys("Ivan")
     input2 = browser.find_element(By.CSS_SELECTOR, "[class='form-control second'][required]" )
     input2.send_keys("Petrov")
     input3 = browser.find_element(By.CSS_SELECTOR, "input.third")
     input3.send_keys("m@test.ru")
     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
     button.click()
     
     time.sleep(2)  
     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1") 
     welcome_text = welcome_text_elt.text  

     self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "No Test")
     
if __name__ == "__main__":
    unittest.main()

    



