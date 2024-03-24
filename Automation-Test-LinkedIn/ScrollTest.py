from selenium import webdriver
import allure
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@allure.severity(allure.severity_level.NORMAL)

class TestGoogleSearch:

    driver = webdriver.Firefox()

    driver.get("https://www.linkedin.com/")

    search = driver.find_element("id","session_key")
    search.send_keys("bcanhck29@gmail.com")
    time.sleep(1)
    search = driver.find_element("id","session_password")
    search.send_keys("qwerty12345")
    time.sleep(1)
    search.submit()
    time.sleep(60)
    driver.execute_script("window.scrollTo(0,25;")

    time.sleep(0.5)

new_height = driver.execute_script("return document.body.scrollHeight")



time.sleep(20)
driver.close()


