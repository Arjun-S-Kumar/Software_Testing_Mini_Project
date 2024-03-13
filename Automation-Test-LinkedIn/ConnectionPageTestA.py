import time
import allure
from selenium import webdriver

@allure.feature("LinkedIn Connection Feature")
@allure.story("Open Connection Page")
@allure.title("Test Connection Page Functionality")
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

    with allure.step("Verify Connection Page"):
        search = driver.find_element("xpath",
                                     "/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div/ul/li/a/div")
        search.click()

        time.sleep(5)

    with allure.step("Close browser"):
        driver.close()


