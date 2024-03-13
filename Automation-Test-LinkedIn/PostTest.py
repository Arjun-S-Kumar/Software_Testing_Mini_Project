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
search = driver.find_element("xpath",'//*[@id="ember27"]')
search.click()

search = driver.find_element("xpath", "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div[1]")
search.send_keys("This is my post content")

# Add hashtags (optional)
search.send_keys(Keys.SHIFT + Keys.ENTER)

# Click on the "Post" button
search = driver.find_element("xpath", "/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button/span")
search.click()

time.sleep(20)
driver.close()
