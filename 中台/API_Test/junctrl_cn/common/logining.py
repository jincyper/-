from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By


# from common.getdriver import GetDriver


# # edge浏览器测试
# class Logining:
#     def __init__(self):
#         self.driver = webdriver.Edge()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(8)
#         self.driver.get('https://test.junctrl.cn/')
#         self.driver.find_element(by=By.XPATH, value="//input[@placeholder='用户名']").send_keys('agenttest')
#         self.driver.find_element(by=By.XPATH, value="//input[@placeholder='密码']").send_keys('agenttest123')
#         self.driver.find_element(by=By.XPATH,
#                                  value="//button[@class='ant-btn ant-btn-primary ant-btn-lg login-button']").click()
#         sleep(5)
#
#         self.driver = webdriver.EdgeOptions()
#         # 关闭密码提示框
#         self.driver.add_experimental_option("prefs", {
#             "download.prompt_for_download": False,
#             "download.directory_upgrade": True,
#             "safebrowsing.enabled": True,
#             "credentials_enable_service": False,
#             "profile.password_manager_enabled": False
#         })
#         # 关闭被控制提示
#         self.driver.add_experimental_option("excludeSwitches", ['enable-automation'])
#         sleep(5)
#
#
# if __name__ == '__main__':
#     get = Logining()


# chrome浏览器测试
class Logining:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://test.junctrl.cn/")
        self.driver.find_element(by=By.XPATH, value="//input[@placeholder='用户名']").send_keys('agenttest')
        self.driver.find_element(by=By.XPATH, value="//input[@placeholder='密码']").send_keys('agenttest123')
        self.driver.find_element(by=By.XPATH,
                                 value="//button[@class='ant-btn ant-btn-primary ant-btn-lg login-button']").click()

        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 关闭被控制提示
        # options.add_argument("--no-sandbox")  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        self.driver = webdriver.Chrome(options=options)

        sleep(5)


if __name__ == '__main__':
    get = Logining()
