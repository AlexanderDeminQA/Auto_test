from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

link = 'https://arenum.io/ru'

@pytest.fixture
def browser():
    print("Браузер открылся")
    browser = webdriver.Chrome()
    return browser


class TestGoogle():
    def test_redirect_link(self, browser):
        browser.get(link)
        button1 = browser.find_element(By.XPATH, '//div [@class="sb-btn-inner"]')
        button1.click()
        time.sleep(3)
        test1 = browser.find_element(By.XPATH, '//h3 [@class="sb-title"]')
        save1 = test1.text
        assert save1 == 'Прошедшие'



