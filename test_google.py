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
    #@pytest.mark.smok
    #@pytest.mark.skip
    def test_redirect_link(self, browser):
        browser.get(link)
        button1 = browser.find_element(By.XPATH, '//div [@class="sb-btn-inner"]')
        button1.click()
        test1 = browser.find_element(By.XPATH, '//h3 [@class="sb-title"]')
        save1 = test1.text
        assert save1 == 'Прошедшие'
    @pytest.mark.xfail
    def test_no_button(self, browser):
        browser.get(link)
        button3 = browser.find_element(By.XPATH, '//div[@class="sb-t-title"]')
        assert button3, "No button"

class TestArenum():
   # @pytest.mark.regres
    #@pytest.mark.win10
    def test_button_click(self, browser):
        browser.get(link1)
        button2 = browser.find_element(By.XPATH, '//div[@class="sb-t-title"]')
        text1 = button2.text
        assert text1 == 'Flappy Doggo Fast Cup'



