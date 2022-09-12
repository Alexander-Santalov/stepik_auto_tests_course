from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_lesson1_step5():
    link = "https://suninjuly.github.io/math.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.ID, "robotsRule").click()
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))


def test_lesson1_step7():
    link = "http://suninjuly.github.io/get_attribute.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x = browser.find_element(By.TAG_NAME, "img").get_attribute("valuex")
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.ID, "robotsRule").click()
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson2_step3():
    link = "http://suninjuly.github.io/selects1.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x = int(browser.find_element(By.ID, "num1").text)
        y = int(browser.find_element(By.ID, "num2").text)
        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value(str(x+y))
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson2_step6():
    link = "http://SunInJuly.github.io/execute_script.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        # browser.execute_script("window.scrollBy(0, 100);")
        browser.find_element(By.ID, "robotsRule").click()
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson2_step8():
    link = "http://suninjuly.github.io/file_input.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)

        browser.find_element(By.NAME, "firstname").send_keys("Alex")
        browser.find_element(By.NAME, "lastname").send_keys("Alex")
        browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("Alex@ya.ru")
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir + "\Data", '1.txt')
        browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson3_step4():
    link = "http://suninjuly.github.io/alert_accept.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.TAG_NAME, "button").click()
        browser.switch_to.alert.accept()
        x = browser.find_element(By.ID, "input_value").text
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson3_step6():
    link = "http://suninjuly.github.io/redirect_accept.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        browser.find_element(By.TAG_NAME, "button").click()
        browser.switch_to.window(browser.window_handles[1])
        x = browser.find_element(By.ID, "input_value").text
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


def test_lesson4_step8():
    link = "http://suninjuly.github.io/explicit_wait2.html"

    try:
        browser = webdriver.Chrome()
        browser.get(link)
        WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100"))
        browser.find_element(By.ID, "book").click()
        x = browser.find_element(By.ID, "input_value").text
        y = calc(x)
        browser.find_element(By.ID, "answer").send_keys(y)
        browser.find_element(By.ID, "solve").click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()