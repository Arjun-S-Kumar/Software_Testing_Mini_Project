import time
from selenium import webdriver

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
search = driver.find_element("xpath","/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/section/header/h2/a/span[1]")
search.click()



time.sleep(20)
driver.close()


