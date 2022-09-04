from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def test_lesson6_step4():
    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        browser.find_element(By.NAME, "last_name").send_keys("Petrov")
        browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
        browser.find_element(By.ID, "country").send_keys("Russia")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson6_step5():
    link = "http://suninjuly.github.io/find_link_text"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))).click()

        browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        browser.find_element(By.NAME, "last_name").send_keys("Petrov")
        browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
        browser.find_element(By.ID, "country").send_keys("Russia")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson6_step7():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.CSS_SELECTOR, "input")
        for element in elements:
            element.send_keys("1")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson6_step8():
    link = "http://suninjuly.github.io/find_xpath_form"
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        browser.find_element(By.NAME, "last_name").send_keys("Petrov")
        browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
        browser.find_element(By.ID, "country").send_keys("Russia")
        browser.find_element(By.XPATH, ".//button[@type='submit']").click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson6_step11():
    try:
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first").send_keys("Alex")
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, ".third").send_keys("bolid@ya.ru")
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()