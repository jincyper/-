import unittest
from common.getdriver import GetDriver
from time import sleep
from selenium.webdriver.common.by import By


class LoginPage(GetDriver):
    def open(self):
        self.driver.get('https://test.junctrl.cn/')

    def login(self, username, password):
        self.driver.find_element(by=By.XPATH, value="//input[@placeholder='用户名']").send_keys(username)
        self.driver.find_element(by=By.XPATH, value="//input[@placeholder='密码']").send_keys(password)
        self.driver.find_element(by=By.XPATH,
                                 value="//button[@class='ant-btn ant-btn-primary ant-btn-lg login-button']").click()
        # 获取当前处于总部或店铺的名称
        txt = self.driver.find_element("xpath",
                                       '//*[@id="app"]/div/section/section/header[2]/div/a/button/span[2]').text

    def login_check(self):
        try:
            self.driver.find_element(by=By.XPATH, value="//h1[@class='brand']")
            return True
        except Exception as e:
            # print(e)
            return False

    def close(self):
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    login = LoginPage()
    login.open()
    login.login('agenttest', 'agenttest123')
    print(login.login_check())
    login.close()
