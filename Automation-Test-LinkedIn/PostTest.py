import time
from selenium import webdriver
from selenium.webdriver import Keys

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/")
search = driver.find_element("id","session_key")
search.send_keys("bcanhck29@gmail.com")
time.sleep(1)
search = driver.find_element("id","session_password")
search.send_keys("qwerty12345")
search.submit()

time.sleep(60)
search = driver.find_element("xpath",'//*[@id="ember26"]')
search.click()

time.sleep(5)
driver.close()
