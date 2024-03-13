import time
import allure
from selenium import webdriver

@allure.feature("LinkedIn Profile Page Feature")
@allure.story("Open Profile Page")
@allure.title("Test Profile Page Functionality")
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
        search = driver.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div[1]/div[1]/a/div[2]")
        search.click()


    with allure.step("Close browser"):
        driver.close()


