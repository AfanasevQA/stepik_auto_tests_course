from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

try: 
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.XPATH, "/html/body/div/div/div/button")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/div/div[1]/h5[2]"),'$100')
    )
    button.click()

    x_element = browser.find_element(By.XPATH,"/html/body/form/div/div/div/label/span[2]")
    x = x_element.text
    y = calc(x)
    print(y)
    
    input=browser.find_element(By.XPATH,"/html/body/form/div/div/div/input")
    input.send_keys(y)
    button = browser.find_element(By.XPATH,"/html/body/form/div/div/button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()