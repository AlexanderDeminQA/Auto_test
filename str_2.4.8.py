from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    br = webdriver.Chrome()
    br.get(link)
    oj = WebDriverWait(br, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = br.find_element(By.ID, 'book')
    button.click()
    zn = br.find_element(By.ID, 'input_value')
    a = zn.text
    b = calc(a)
    button1 = br.find_element(By.ID, 'answer')
    button1.send_keys(b)
    input1 = br.find_element(By.CSS_SELECTOR, "#solve.btn.btn-primary")
    input1.click()


finally:
    time.sleep(4)
    br.quit()
