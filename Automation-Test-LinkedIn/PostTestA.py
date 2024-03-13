import time
import allure
from selenium import webdriver

@allure.feature("Post Feature")
@allure.story("Create Post")
@allure.title("Test Post Functionality")
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

    with allure.step("Navigate to Post"):
        search = driver.find_element("xpath", '//*[@id="ember26"]')
        search.click()

    with allure.step("Create post"):
        # Create a new post

    with allure.step("Enter post content"):
        # Enter the post content

    with allure.step("Submit post"):
        # Click the submit button

    with allure.step("Verify post created"):
        # Verify that the post was created successfully

    with allure.step("Close browser"):
        driver.close()


