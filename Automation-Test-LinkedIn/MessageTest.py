from selenium import webdriver
import allure
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@allure.severity(allure.severity_level.NORMAL)

class TestGoogleSearch:

    @allure.severity(allure.severity_level.MINOR)
    def Message(self):

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
        search = driver.find_element("xpath","/html/body/div[5]/div[4]/aside[1]/div[1]/section/div[2]/div/div/div")
        search.click()

        search = driver.find_element("xpath","/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/div[3]/div/div[1]/div[1]")
        search.send_keys("qwerty12345")
        search = driver.find_element("xpath","/html/body/div[5]/div[4]/aside[1]/div[2]/div[1]/div[2]/div/form/footer/div[2]/div[1]/button")
        search.submit()

        time.sleep(20)
        driver.close()
