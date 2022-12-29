from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

link = "https://stepik.org/lesson/236895/step/1"

class TestLoginStepik():
    def test_login_Stepik(self, browser):
        browser.get(link)
        button1 = browser.find_element(By.XPATH, '//a[@id="ember33"]')
        button1.click()
        with open("C:\\Users\\schur\\selenium_course\\Block_2\\login.txt") as file_in:
            lines = []
            for line in file_in:
                lines.append(line)
        input_login = browser.find_element(By.XPATH, '//input [@id="id_login_email"]')
        input_login.send_keys(lines[0])
        input_password = browser.find_element(By.XPATH, '//input [@id="id_login_password"]')
        input_password.send_keys(lines[1])
        button2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
        button2.click()
        input_wait = browser.find_element(By.XPATH, '//textarea[@id="ember87"]')
        input_wait.send_keys("Passet")
        button3 = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
        button3.click()
        time.sleep(3)





