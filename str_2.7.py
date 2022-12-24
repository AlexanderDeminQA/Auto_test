from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    br = webdriver.Chrome()
    br.get(link)
    snd = br.find_element(By.XPATH, '//img[@id="treasure"]')
    zn1 = snd.get_attribute("valuex")
    b = calc(zn1)
    input1 = br.find_element(By.XPATH, '//input[@id="answer"]')
    input1.send_keys(b)
    time.sleep(1)
    chek = br.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    chek.click()
    time.sleep(1)
    chek1 = br.find_element(By.XPATH, '//input[@id="robotsRule"]')
    chek1.click()
    time.sleep(1)
    chek2 = br.find_element(By.XPATH, '//button[@class="btn btn-default"]')
    chek2.click()
    time.sleep(1)

finally:

    #time.sleep(5)
    br.quit()


