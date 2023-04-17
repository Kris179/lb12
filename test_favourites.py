from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser=webdriver.Chrome()
#загружаем страницу
browser.get('https://www.zookorm33.ru/')
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
time.sleep(5)


#ищем кнопку добавления в избранное
favourites = browser.find_element(by=By.XPATH, value='/html/body/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[4]/button[3]')
favourites.click()

#ищем кнопку избранное
button_favourites=browser.find_element(by=By.XPATH, value='/html/body/header/div[2]/div[2]/div[4]/div')
button_favourites.click()

#ждем загрузку страницы закладки
loading = WebDriverWait(browser, 10).until(
        EC.title_is('Мои закладки')
    )

#ищем контейнер статьи по id
article1 = browser.find_element(by=By.CLASS_NAME, value='product-thumb__name')

try:
# Проверка что пользователь находится на главной странице сайта
    assert 'Мои закладки' in browser.title
# Проверка что на странице присутствует избранный товар
    assert article1.text == 'Forza10 Maxi Diet сухой корм для взрослых собак крупных пород при аллергии из рыбы с микрокапсулами - 12 кг'
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
# Закрываем браузер
browser.close()