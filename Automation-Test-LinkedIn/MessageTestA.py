import time
import allure
from selenium import webdriver

@allure.feature("Message Feature")
@allure.story("Send Message")
@allure.title("Test Message Functionality")
def test_message():
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

    with allure.step("Navigate to Messages"):
        search = driver.find_element("xpath", "/html/body/div[5]/div[4]/aside[1]/div[1]/section/div[2]/div/div/div")
        search.click()
    with allure.step("Enter message content"):
        search = driver.find_element("xpath",
                                     "/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/div[3]/div/div[1]/div[1]")
        search.send_keys("Hello")

    with allure.step("Send message"):
        search = driver.find_element("xpath",
                                     "/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/footer/div[2]/div[1]/button")
        search.submit()

    time.sleep(5)

    with allure.step("Close browser"):
        driver.close()
