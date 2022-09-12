from selenium.webdriver.common.by import By


def test_btn_add_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    equal = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"))
    assert equal == 1, f"Ожидаемый результат {1}, Фактический {equal}"
