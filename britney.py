from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.southwest.com/loyalty/myaccount/")
driver.find_element("xpath", "/html/body/div[3]/div/div/div/div[2]/div[1]/div[2]/div[1]/span/span/div/div/button").click()
driver.find_element("id", "username").send_keys("britneychanp")
driver.find_element("id", "password").send_keys("ScrappyDoo12!")
driver.find_element("id", "login-form--submit-button").click()
time.sleep(5)
driver.quit()