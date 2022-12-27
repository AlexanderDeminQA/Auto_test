from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unitest

class TestAbs(unitest.TestCase):

    link = 'http://suninjuly.github.io/registration1.html'
    br = webdriver.Chrome()
    br.get(link)

    in1 = br.find_element(By.CLASS_NAME, 'form-control.first')  # Заполнение формы обязательных полей и подтверждение
    in1.send_keys("Alexander")
    time.sleep(1)
    in1 = br.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    in1.send_keys("Demin")
    time.sleep(1)
    in2 = br.find_element(By.CLASS_NAME, 'form-control.third')
    in2.send_keys("adafaf@dsf.com")
    time.sleep(1)
    but = br.find_element(By.CLASS_NAME, 'btn.btn-default')
    but.click()
    time.sleep(1)

    sucses_one = br.find_element(By.TAG_NAME, 'h1')         # Получение надписи об успешной регистрации
    sucses = sucses_one.text
    self.assertEqual( "Congratulations! You have successfully registered!" == sucses )  # Проверка надписи

link = 'http://suninjuly.github.io/registration2.html'
br = webdriver.Chrome()
br.get(link)

in1 = br.find_element(By.CLASS_NAME, 'form-control.first')  # Заполнение формы обязательных полей и подтверждение
in1.send_keys("Alexander")
time.sleep(1)
in1 = br.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
in1.send_keys("Demin")
time.sleep(1)
in2 = br.find_element(By.CLASS_NAME, 'form-control.third')
in2.send_keys("adafaf@dsf.com")
time.sleep(1)
but = br.find_element(By.CLASS_NAME, 'btn.btn-default')
but.click()
time.sleep(1)

sucses_one = br.find_element(By.TAG_NAME, 'h1')         # Получение надписи об успешной регистрации
sucses = sucses_one.text
assert "Congratulations! You have successfully registered!" == sucses   # Проверка надписи

time.sleep(5)
br.quit()





