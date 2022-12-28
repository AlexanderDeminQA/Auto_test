from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

link = 'http://suninjuly.github.io/registration1.html'
link1 = 'http://suninjuly.github.io/registration2.html'

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class Testlink():
    def test_link(self, browser):
        browser.get(link)

        in1 = browser.find_element(By.CLASS_NAME, 'form-control.first')  # Заполнение формы обязательных полей и подтверждение
        in1.send_keys("Alexander")
        time.sleep(1)
        in1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        in1.send_keys("Demin")
        time.sleep(1)
        in2 = browser.find_element(By.CLASS_NAME, 'form-control.third')
        in2.send_keys("adafaf@dsf.com")
        time.sleep(1)
        but = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
        but.click()
        time.sleep(1)

        sucses_one = browser.find_element(By.TAG_NAME, 'h1')  # Получение надписи об успешной регистрации
        sucses = sucses_one.text
        assert "Congratulations! You have successfully registered!" == sucses

    def test_link1(self, browser):
        browser.get(link)

        in1 = browser.find_element(By.CLASS_NAME, 'form-control.first')  # Заполнение формы обязательных полей и подтверждение
        in1.send_keys("Alexander")
        time.sleep(1)
        in1 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        in1.send_keys("Demin")
        time.sleep(1)
        in2 = browser.find_element(By.CLASS_NAME, 'form-control.third')
        in2.send_keys("adafaf@dsf.com")
        time.sleep(1)
        but = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
        but.click()
        time.sleep(1)

        sucses_one = browser.find_element(By.TAG_NAME, 'h1')  # Получение надписи об успешной регистрации
        sucses = sucses_one.text
        assert "Congratulations! You have successfully registered!" == sucses

