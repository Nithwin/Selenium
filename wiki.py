from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()


try:
    driver.get("https://www.wikipedia.org")
    wait = WebDriverWait(driver,10)
    search_bar = wait.until(EC.presence_of_element_located((By.ID, "searchInput")))
    #search_bar = driver.find_element(By.ID, "searchInput")
    search_bar.send_keys("Monkey D Luffy")
    search_bar.send_keys(Keys.ENTER)
    print("Successfully!")
    time.sleep(10)
finally:
    driver.quit()