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
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
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


def login(login, password):
    set_value(driver=driver, id="user-name", value=login)
    set_value(driver=driver, id="password", value=password)
    click_element(driver=driver, id="login-button")


driver = get_driver()
open_url(driver=driver, url=URL)
login(login=LOGIN, password=PASSWORD)

driver.quit()
