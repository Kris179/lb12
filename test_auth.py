from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser=webdriver.Chrome()
#загружаем страницу
browser.get('https://www.zookorm33.ru/o_nas')
time.sleep(2)

#ищем кнопку открытия меню пользователя
button_menu_vxod=browser.find_element(by=By.CSS_SELECTOR, value='#account > button')
button_menu_vxod.click()
time.sleep(2)


#ищем кнопку входа
vxod=browser.find_element(by=By.CSS_SELECTOR, value='#account > ul > li:nth-child(1) > a')
vxod.click()
time.sleep(2)

# заполняем поле логин, привязываемся к элементу через его имя
username=browser.find_element(by=By.CSS_SELECTOR, value='#modal-login-form > div > div > div.modal-body > form > input:nth-child(1)')
username.send_keys('sobolenkokristina13@gmail.com')

# заполняем поле пароля, привязываемся к элементу через его id
password=browser.find_element(by=By.CSS_SELECTOR, value='#modal-login-form > div > div > div.modal-body > form > input:nth-child(2)')
password.send_keys('29012004ns')
#Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
vhod = browser.find_element(by=By.CSS_SELECTOR, value='#modal-login-form > div > div > div.modal-body > button')
vhod.click()
time.sleep(2)


try:
    # Проверка что на странице присутствует полное имя пользователя
    assert "Кристина" in browser.page_source
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
# Закрываем браузер
browser.close()