import time
import allure
from selenium import webdriver

@allure.feature("LinkedIn Article Feature")
@allure.story("Open Article Page")
@allure.title("Test Article Page Functionality")
def test_post():
    with allure.step("Open browser"):
        driver = webdriver.Firefox()
        driver.get("https://www.linkedin.com/")

    with allure.step("Enter username"):
        search = driver.find_element("id", "session_key")
        search.send_keys("bcanhck29@gmail.com")

    with allure.step("Enter password"):
        search = driver.find_element("id", "session_password")
        search.send_keys("qwerty12345")

    with allure.step("Submit login form"):
        search.submit()

    time.sleep(50)

    with allure.step("Verify Groups Page"):
        driver.get("https://www.linkedin.com/article/new/")

    with allure.step("Close browser"):
        driver.close()


