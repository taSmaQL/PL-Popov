###
Код был написан не для корыстных целей, контент предназначен только для ознакомления.
###
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time
import requests
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
count=int(input('Сколько вопросов?: '))
matan = input('Присутствует ли в вопросах картинки?: ')
attempt = 0
max_attempts = 5

while attempt < max_attempts:
    try:
        driver.get(url=url)
        break
    except WebDriverException:
        attempt += 1
        print(f"Не удалось зайти на сайт. Попытка {attempt} из {max_attempts}.")
        time.sleep(8)
else:
    driver.quit()
try:
    login_input = driver.find_element(By.ID,'username')
    login_input.clear()
    login_input.send_keys(students_username)
    password_input = driver.find_element(By.ID,'password')
    password_input.clear()
    password_input.send_keys(students_password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.get(url=object)
    time.sleep(1)
    amgis = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']").click()
    time.sleep(2)
    # Новая вкладка.
    driver.switch_to.window(driver.window_handles[1]) 
    driver.maximize_window()
    time.sleep(5)
    # Копируем:
    unique_answers = set()
    all_text = ""
    answers = {}
    if matan in ['Да', 'ДА', 'да']:
        for i in range(1, count + 1):
            sigma = driver.find_element(By.XPATH,f"(//span[@class='thispageholder'])[{i}]").click()
            test_element = driver.find_element(By.XPATH, "//div[@class='formulation clearfix']")
            images = test_element.screenshot_as_png
            filename = f'image_{i}.png'
            with open(filename, 'wb') as f:
                f.write(images)
    else:
        for i in range(1, count + 1):
            sigma = driver.find_element(By.XPATH,f"(//span[@class='thispageholder'])[{i}]").click()
            question_element = driver.find_element(By.XPATH, "//div[@class='qtext']")
            question_text = question_element.text
            try:
                answer_element = driver.find_element(By.XPATH,'//div[@class="answer"]')
                answer_text = answer_element.text 
            except NoSuchElementException:
                try:
                    answer_elements = driver.find_elements(By.XPATH, '//tr[@class="r0"]/td/p | //tr[@class="r1"]/td/p')
                    for index, answer_element in enumerate(answer_elements):
                        answer_text = answer_element.text
                        answers[answer_text] = f'{index + 1}-й вариант ответа'
                except NoSuchElementException:
                    print('Элементы с классом answer не найдены.')
except Exception as ex:
    print(ex)
finally: 
    driver.close()
    driver.quit()
