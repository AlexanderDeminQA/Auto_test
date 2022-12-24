from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    br = webdriver.Chrome()
    br.get(link)
    vk = br.find_element(By.CSS_SELECTOR, '[type="submit"]')
    vk.click()
    new_window = br.window_handles[1]
    br.switch_to.window(new_window)
    zn = br.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    a = zn.text
    b = calc(a)
    input1 = br.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input1.send_keys(b)
    sub = br.find_element(By.CSS_SELECTOR, '[type="submit"]')
    sub.click()
    alert = br.switch_to.alert
    alert1 = alert.text
    print(alert1)


finally:
    time.sleep(6)
    br.quit()
