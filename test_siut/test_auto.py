from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math




class TestLoginStepik():
    @pytest.mark.parametrize('get_link', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
    def test_link(self, get_link, browser):
        link = f"https://stepik.org/lesson/{get_link}/step/1"
        answer = math.log(int(time.time()))
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
        time.sleep(3)
        input_wait = browser.find_element(By.XPATH, '[style="height: 80px;"]')
        time.sleep(3)
        input_wait.send_keys(answer)
        button3 = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
        time.sleep(3)
        button3.click()
        time.sleep(3)