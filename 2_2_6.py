from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):


try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    browser.get(link)
	    
    element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла