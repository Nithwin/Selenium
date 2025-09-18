from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")

try:
    # This is the key part!
    # Wait a maximum of 10 seconds for the element to become visible.
    wait = WebDriverWait(driver, 10)
    input_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "gLFyf"))
    )

   # input_password = wait.until(EC.visibility_of_element_located((By.NAME, "password")))

    # Once the element is found, the script continues
    input_element.send_keys("Monkey D Luffy" + Keys.ENTER)
    #input_password.send_keys("test1234")


    time.sleep(5) 

finally:
    
    driver.quit()