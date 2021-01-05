import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import secrets

driver = webdriver.Firefox(executable_path="/home/potter/.local/share/firefox/geckodriver")

# Navigate to Url
driver.get("https://vk.com")

login_field = driver.find_element(By.ID, "index_email")
login_field.click()
login_field.send_keys(secrets.login)

password_field = driver.find_element(By.ID, "index_pass")
password_field.click()
password_field.send_keys(secrets.password)

button = driver.find_element(By.ID, "index_login_button")
button.click()

time.sleep(3)

person_id = "264390313"

driver.get("https://vk.com/im?sel=" + person_id)

message_box = driver.find_element(By.ID, "im_editable" + person_id)
message_box.click()
message_box.send_keys(":D" + Keys.ENTER)