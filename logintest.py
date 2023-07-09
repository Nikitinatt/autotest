from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.saucedemo.com/"
LOGIN = "standard_user"
PASSWORD = "secret_sauce"


def get_driver():
    chrome_options = Options()

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    return driver


def open_url(driver, url):
    driver.get(url)


def get_element(driver, id):
    return driver.find_element(By.ID, id)


def click_element(driver, id):
    element = get_element(driver=driver, id=id)
    element.click()


def set_value(driver, id, value):
    element = get_element(driver=driver, id=id)
    element.send_keys(value)


def login(driver, login, password):
    set_value(driver=driver, id="user-name", value=login)
    set_value(driver=driver, id="password", value=password)
    click_element(driver=driver, id="login-button")


driver = get_driver()
open_url(driver=driver, url=URL)
login(driver=driver, login=LOGIN, password=PASSWORD)
click_element(driver, id="add-to-cart-sauce-labs-backpack")
click_element(driver, id="shopping_cart_container")
click_element(driver, id="checkout")

driver.quit()
