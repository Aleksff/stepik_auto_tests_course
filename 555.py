from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control")
    input1.send_keys(y)
    check = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check.click()
    radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла