import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import HTMLTestRunner

class login(unittest.TestCase):
    def test_log(self):
        driver = webdriver.Edge()
        driver.get('https://test.junctrl.cn/')
        driver.maximize_window()
        sleep(3)

        log_title = '钧控门店管家'
        self.assertIn(log_title, driver.title, '钧控门店管家')

        driver.find_element(by=By.XPATH, value="//input[@placeholder='用户名']").send_keys("agenttest")
        sleep(1)
        driver.find_element(by=By.XPATH, value="//input[@placeholder='密码']").send_keys("agenttest123")
        sleep(1)
        driver.find_element(by=By.XPATH, value="//button[@class='ant-btn ant-btn-primary ant-btn-lg login-button']").click()
        sleep(2)

        # driver.quit()

if __name__ == '__main__':
    yl = r'./'
    discover = unittest.defaultTestLoader.discover(yl, 'test_log.py')

    file_path = './report/send_login.html'
    with open(file_path, 'wb') as rf:
        runner = HTMLTestRunner.HTMLTestRunner(stream=rf, title='jk测试报告', description='自动化测试')
        runner.run(discover)
