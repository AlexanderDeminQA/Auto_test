from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    br = webdriver.Chrome()
    br.get(link)
    but = br.find_element(By.CSS_SELECTOR, "[type='submit']")
    but.click()
    time.sleep(1)
    alert = br.switch_to.alert
    alert.accept()
    zn = br.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    a = zn.text
    b = calc(a)
    str1 = br.find_element(By.CSS_SELECTOR, '[id="answer"]')
    str1.send_keys(b)
    but1 = br.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    but1.click()

finally:
    time.sleep(3)
    br.quit()
