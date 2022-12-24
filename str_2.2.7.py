import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    br = webdriver.Chrome()
    br.get(link)
    input1 = br.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys('Alexander')
    input2 = br.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys('Demin')
    input3 = br.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys('schurick.don@gnair.com')
    cr_dir = os.path.abspath(os.path.dirname(__file__))
    na_dir = "name.txt"
    file_dir = os.path.join(cr_dir, na_dir)
    bat = br.find_element(By.CSS_SELECTOR, "[id='file']")
    bat.send_keys(file_dir)
    but1 = br.find_element(By.CSS_SELECTOR, '[type="submit"]')
    but1.click()

finally:
    time.sleep(3)
    br.quit()
