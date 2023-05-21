from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_find_basket_button(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group,btn.btn-default")
