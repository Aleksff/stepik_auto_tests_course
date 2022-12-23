from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x1 = browser.find_element(By.ID, "num1")
    y1 = browser.find_element(By.ID, "num2")
    x= x1.text
    y= y1.text
    s1 = int(x)
    s2 = int(y)
    sum = s1 + s2
    sum_el= str(sum)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text('%s' % sum_el)
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла