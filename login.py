from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)
    username = wait.until(EC.presence_of_element_located((By.NAME,"username")))
    username.send_keys("tomsmith")
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys("SuperSecretPassword!")
    login_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[type='submit']")))
    login_btn.click()
    success_message = wait.until(EC.presence_of_element_located((By.ID,"flash")))
    if success_message.is_displayed():
        print("Login success")
    else:
        print("Login Failed")
    time.sleep(4)
finally:
    driver.quit()