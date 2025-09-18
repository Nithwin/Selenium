from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSessionIdException
import time
import send_email
driver = webdriver.Chrome()

try:
    driver.get("https://nithwin-dashboard.vercel.app/login")
    wait = WebDriverWait(driver,10)
    username = wait.until(EC.presence_of_element_located((By.NAME,"email")))
    username.send_keys("test@gmal.com")

    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.send_keys("test1234")

    btn = wait.until(EC.presence_of_element_located((By.TAG_NAME,"button")))
    btn.click()

    startDate = wait.until(EC.presence_of_element_located((By.ID,"startDate")))
    if startDate.is_displayed():
        send_email.send_email("Your application working properly the given email and password matched with the Database")
    else:
        send_email.send_email("Error! the given email and password does match with your db check your db subscription")
    time.sleep(10)

except TimeoutException or InvalidSessionIdException:
    send_email.send_email("Error! the given email and password does match with your db check your db subscription")
finally:
    driver.quit()