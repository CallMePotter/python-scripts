import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import secrets

driver = webdriver.Firefox(executable_path="/home/potter/.local/share/firefox/geckodriver")

# Navigate to Url
driver.get("https://vk.com")

# Enter login info
login_field = driver.find_element(By.ID, "index_email")
login_field.send_keys(secrets.login)

# Enter password info
password_field = driver.find_element(By.ID, "index_pass")
password_field.send_keys(secrets.password)

# Press login button
button = driver.find_element(By.ID, "index_login_button")
button.click()

# Wait for page to load
time.sleep(3)

ids = ["558904070"]

for person in ids:
    driver.get("https://vk.com/im?sel=" + person)

    message_box = driver.find_element(By.ID, "im_editable" + person)
    message_box.send_keys(":D" + Keys.ENTER)

    time.sleep(5) # sleep so you don't trigger anti-bot system
