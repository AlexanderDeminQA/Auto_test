from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    br = webdriver.Chrome()
    br.get(link)
    sum1 = br.find_element(By.CSS_SELECTOR, "#num1.nowrap")
    sum2 = br.find_element(By.CSS_SELECTOR, "#num2.nowrap")
    a, b = sum1.text, sum2.text
    c = int(a)+int(b)
    t = str(c)
    sel = Select(br.find_element(By.CSS_SELECTOR, "#dropdown.custom-select"))
    sel.select_by_value(t)
    sub = br.find_element(By.XPATH, "//button[@class = 'btn btn-default']")
    sub.click()

finally:
    time.sleep(3)
    br.quit()
