from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

element = driver.find_element_by_name("email")
print(element.is_displayed())
print(element.is_enabled())

element.send_keys("you_email_ID")

password = driver.find_element_by_name("pass")

password.send_keys("Your_facebook_Password")

driver.find_element_by_name("login").click()

time.sleep(5)


driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div[3]/label/input').send_keys("kannada sangha")

driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div[3]/label/input').send_keys(Keys.ENTER)