from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

'''登录成功'''
driver = webdriver.Edge()
driver.get('https://test.junctrl.cn/')
time.sleep(1)
driver.find_element(by=By.XPATH, value="//input[@placeholder='用户名']").send_keys("agenttest")
time.sleep(1)
driver.find_element(by=By.XPATH, value="//input[@placeholder='密码']").send_keys("agenttest123")
time.sleep(1)
driver.find_element(by=By.XPATH, value="//button[@class='ant-btn ant-btn-primary ant-btn-lg login-button']").click()
time.sleep(2)