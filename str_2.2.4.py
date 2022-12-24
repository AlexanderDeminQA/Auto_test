from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    br = webdriver.Chrome()
    br.get(link)
    zn = br.find_element(By.XPATH, "//span[@id='input_value']")
    t = zn.text
    b = calc(t)
    input1 = br.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(b)
    but = br.find_element(By.CSS_SELECTOR, "#robotCheckbox.form-check-input")
    but.click()
    scr = br.find_element(By.CSS_SELECTOR, "#robotsRule.form-check-input")
    br.execute_script("arguments[0].scrollIntoView(true);", scr)
    scr.click()
    but1 = br.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    but1.click()
finally:
    time.sleep(3)
    br.quit()
