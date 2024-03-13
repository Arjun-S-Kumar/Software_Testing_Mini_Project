import time
from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com/")

search = driver.find_element("id","session_key")
search.send_keys("bcanhck29@gmail.com")
search = driver.find_element("id","session_password")
search.send_keys("qwerty12345")


search.submit()
time.sleep(20)
driver.close()

