import time
import allure
from selenium import webdriver

@allure.feature("Login Failure Feature")
@allure.story("Successful Login")
@allure.title("Test Login Functionality")
def test_login():
    with allure.step("Open browser"):
        driver = webdriver.Firefox()
        driver.get("https://www.linkedin.com/")

    with allure.step("Enter username"):
        search = driver.find_element("id", "session_key")
        search.send_keys("lohit.k2307@gmail.com")

    with allure.step("Enter password"):
        search = driver.find_element("id", "session_password")
        search.send_keys("qwerty12345")

    with allure.step("Submit login form"):
        search.submit()

    time.sleep(5)
    with allure.step("Verify login"):
        assert driver.title == "LinkedIn"

    with allure.step("Close browser"):
        driver.close()
