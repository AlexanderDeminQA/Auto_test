from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

link = 'https://arenum.io/ru'
link1 = 'https://arenum.io/ru/scorebeat/tournament/JJbLM4ZYQg-YPpI79Abpkg'

@pytest.fixture()
def browser():
    print(" Браузер открылся")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print(' Браузер закрыт')
    browser.quit()



class TestGoogle():
    @pytest.mark.skip
    def test_redirect_link(self, browser):
        browser.get(link)
        button1 = browser.find_element(By.XPATH, '//div [@class="sb-btn-inner"]')
        button1.click()
        test1 = browser.find_element(By.XPATH, '//h3 [@class="sb-title"]')
        save1 = test1.text
        assert save1 == 'Прошедшие'

class TestArenum():
    @pytest.mark.parametrize('language', ["ru", "en-gb"])
    def test_button_click(self, browser, language):
        link = f'https://arenum.io/{language}/scorebeat/tournament/JJbLM4ZYQg-YPpI79Abpkg'
        browser.get(link)
        button2 = browser.find_element(By.XPATH, '//div[@class="sb-t-title"]')
        text1 = button2.text
        assert text1 == 'Flappy Doggo Fast Cup'

# Тесты parametrize на арене не работают

