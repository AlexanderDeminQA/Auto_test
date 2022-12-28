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
    yield browser
    print(' Браузер закрыт')
    browser.quit()



class TestGoogle():
    #@pytest.mark.smok
    @pytest.mark.skip
    def test_redirect_link(self, browser):
        browser.get(link)
        button1 = browser.find_element(By.XPATH, '//div [@class="sb-btn-inner"]')
        button1.click()
        time.sleep(3)
        test1 = browser.find_element(By.XPATH, '//h3 [@class="sb-title"]')
        save1 = test1.text
        assert save1 == 'Прошедшие'

class TestArenum():
   # @pytest.mark.regres
    #@pytest.mark.win10
    def test_button_click(self, browser):
        browser.get(link1)
        button2 = browser.find_element(By.XPATH, '//div[@class="sb-t-title"]')
        time.sleep(3)
        text1 = button2.text
        assert text1 == 'Flappy Doggo Fast Cup'



