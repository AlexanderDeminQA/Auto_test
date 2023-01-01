from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time
import math

links = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
        ]

class TestLoginStepik():
    @pytest.fixture(scope="function")
    def browser(self):
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        yield browser
        print("\nquit browser..")
        browser.quit()

    @pytest.mark.parametrize('link', links)
    def test_link(self, link, browser):
        browser.get(link)
        answer = str(math.log(int(time.time() - 1.0)))
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
        but_new = browser.find_element(By.XPATH, '//button[@class="again-btn white"]').text
        but_new1 = browser.find_element(By.XPATH, '//button[@class="again-btn white"]').text
        if but_new == 'Решить снова':
            but_start = browser.find_element(By.XPATH, '//button[@class="again-btn white"]')
            but_start.click()
            input_wait = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
            time.sleep(3)
            input_wait.send_keys(answer)
            button3 = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
            time.sleep(3)
            button3.click()
            time.sleep(3)
            check = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text
            assert check == 'Correct!'
        elif but_new1 == 'Начать сначала (сброс)':
            but_start1 = browser.find_element(By.XPATH, '//button[@class="again-btn white"]')
            but_start1.click()
            time.sleep(3)
            but_flutter = browser.find_element(By.CSS_SELECTOR, '#ember292 >button')
            but_flutter.click()
            input_wait = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
            time.sleep(3)
            input_wait.send_keys(answer)
            button3 = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
            time.sleep(3)
            button3.click()
            time.sleep(3)
            check = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text
            assert check == 'Correct!'
        else:
            input_wait = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
            time.sleep(3)
            input_wait.send_keys(answer)
            button3 = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
            time.sleep(3)
            button3.click()
            time.sleep(3)
            check = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text
            assert check == 'Correct!'
