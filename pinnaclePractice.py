from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.pinnacle.com/en/")
tennis = driver.find_element_by_xpath("//*[@id="Events-Container"]/div[4]/div[3]/div[2]/button")))
tennis.click()
time.sleep(5)
driver.quit()