import time
import allure
from selenium import webdriver

@allure.feature("LinkedIn HastTag Feature")
@allure.story("Open Hashtags Page")
@allure.title("Test Hashtags Page Functionality")
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
        driver.get("https://www.linkedin.com/mynetwork/network-manager/hashtags/")


    with allure.step("Close browser"):
        driver.close()


