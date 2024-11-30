###
Код был написан не для корыстных целей, контент предназначен только для ознакомления.
###
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
useragent = UserAgent()
option = webdriver.ChromeOptions()
option.add_argument(f'user-agent={useragent.chrome}')
driver = webdriver.Chrome(options = option)
url = 'https://education.vsuet.ru/login/index.php'
print('-----------------------------------------------------')
print('Примечание: Выключаем ВПН, Прокси или другие аналоги!')
print('Примечание: Нажимаем на старт теста, после этого код!')
print('-----------------------------------------------------')
students_username=input('Введите ваш логин: ')
students_password=input('Введите ваш пароль: ')
object=input('Введите ссылку с тестом: ')
count=input('Сколько вопросов?: ')
try:
    driver.get(url=url)
    time.sleep(5)

    login_input = driver.find_element(By.ID,'username')
    login_input.clear()
    login_input.send_keys(students_username)
    time.sleep(3)
    password_input = driver.find_element(By.ID,'password')
    password_input.clear()
    password_input.send_keys(students_password)
    time.sleep(3)
    password_input.send_keys(Keys.ENTER)
    time.sleep(4)
    driver.get(url=object)
    time.sleep(3)
    amgis = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
    time.sleep(2)
    # Новая вкладка
    driver.switch_to.window(driver.window_handles[1]) 
    driver.maximize_window()
    time.sleep(5)
    sigma = driver.find_element(By.XPATH,"(//span[@class='thispageholder'])[5]").click()
    time.sleep(3)
    test_element = driver.find_element(By.XPATH, "//div[@class='formulation clearfix']")
    images = test_element.screenshot_as_png
    with open ('test.png','wb') as f:
        f.write(images)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally: 
    driver.close()
    driver.quit()
