"""
Библиотеки:
Selene (обертка над Selenium) - управление браузером
Faker - генерация случайных данных
SymPy - выполнение символьных вычислений
Requests - взаимодействие с сервером по HTTP(S) протоколу напрямую, т.е. в обход клиента
"""

import os

import requests
from faker import Faker
from selene import browser, query
from selene.support.shared.jquery_style import s
from sympy import sympify, symbols

random = Faker()

""" 1й скрипт"""
# Открываем страницу в браузере
browser.open('https://suninjuly.github.io/file_input.html')

# Заполняем поля First name, Last name и Email сгенерированными данными
s('[name="firstname"]').type(random.first_name())
s('[name="lastname"]').type(random.last_name())
s('[name="email"]').type(random.email())

# Прикрепляем файл requirements.txt
s('#file').send_keys(os.path.abspath('../requirements.txt'))
# Нажимаем кнопку Submit
s('button').click()

# Переключаемся на всплывающее уведомление и считываем в нем текст
alert_text = browser.switch_to.alert.text

# Получаем из текста число
num_in_alert = ''
for symbol in alert_text:
    if symbol.isdigit() or symbol == '.':
        num_in_alert += symbol

# Выводим число на печать
print(num_in_alert)
# Закрываем всплывающее уведомление
browser.switch_to.alert.accept()


"""2й скрипт"""
# Открываем страницу в браузере
browser.open('https://suninjuly.github.io/redirect_accept.html')

# Кликаем по "магической" кнопке
s('button.trollface').click()
# Переключаемся на новую вкладку
browser.switch_to_next_tab()

# Считываем формулу и значение x
formula_text = s('label .nowrap').get(query.text).strip()
x_text = s('#input_value').get(query.text).strip()

# Считаем результат по формуле
formula_start = formula_text.find('ln')
formula_end = formula_text.find(',')
formula_text = formula_text[formula_start:formula_end]
formula = sympify(formula_text)

x_int = int(x_text)
x_symbol = symbols('x')
result = str(formula.subs(x_symbol, x_int).evalf())

# Вводим в поле для ответа полученный результат
s('#answer').type(result)
# Нажимаем кнопку Submit
s('button').click()

# Переключаемся на всплывающее уведомление и считываем в нем текст
alert_text = browser.switch_to.alert.text

# Получаем из текста число
num_in_alert = ''
for symbol in alert_text:
    if symbol.isdigit() or symbol == '.':
        num_in_alert += symbol

# Выводим число на печать
print(num_in_alert)
# Закрываем всплывающее уведомление
browser.switch_to.alert.accept()
# Закрываем браузер
browser.quit()


"""3й скрипт"""
# Определяем API: сервер для получения данных о местонахождении МКС
api_url = 'http://api.open-notify.org/iss-now.json'

# Отправляем GET-запрос и сохраняем ответ в переменной response
response = requests.get(api_url)

if (
    response.status_code == 200
):  # Если код ответа на запрос - 200, то смотрим, что пришло в ответе
    print(response.text)
else:
    print(response.status_code)  # При другом коде ответа выводим этот код


"""4й скрипт"""
# Определяем API: сервер для получения интересных данных о разных числах
api_url = 'http://numbersapi.com/'

# Отправляем GET-запрос с числом 42 и сохраняем ответ в переменной response
response = requests.get(api_url + '42')
print(response.text)
