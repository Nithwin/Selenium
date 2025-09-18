from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()


try:
    driver.get("https://www.wikipedia.org")
    search_bar = driver.find_element(By.ID, "searchInput")
    search_bar.send_keys("Monkey D Luffy")
    search_bar.send_keys(Keys.ENTER)
    print("Successfully!")
    time.sleep(10)
finally:
    driver.quit()