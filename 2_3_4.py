from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла