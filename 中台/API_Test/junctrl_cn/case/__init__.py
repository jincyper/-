from selenium import webdriver
from time import sleep

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://test.junctrl.cn/")

sleep(5)
driver.quit()
