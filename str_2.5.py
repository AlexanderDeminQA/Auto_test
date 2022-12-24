from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'https://suninjuly.github.io/math.html'

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    br = webdriver.Chrome()                                     # Вычисление переменной
    br.get(link)
    zn = br.find_element(By.XPATH, "//img[@id='treasure']")
    zn1 = zn.get_attribute("valuex")
    a = zn1.text
    b = calc(a)
    input1 = br.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(b)
    time.sleep(2)
    chek1 = br.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    chek1.click()
    time.sleep(2)
    but = br.find_element(By.XPATH, "//input[@id='robotsRule']")
    but.click()
    time.sleep(2)
    but1 = br.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    but1.click()
    time.sleep(2)

finally:
    time.sleep(5)
    br.quit()

