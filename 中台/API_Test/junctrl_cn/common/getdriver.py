# 实例化edge浏览器
# from selenium import webdriver
# from msedge.selenium_tools import EdgeOptions, Edge
# 把实例化的步骤写在构造方法里面.后续在实例化这个类的对象的同时就拥有了driver
# class GetDriver:
#     def __init__(self):
#         self.driver = webdriver.Edge()
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(5)
#
#         self.driver = webdriver.EdgeOptions()
#         # 无头模式
#         # ch_op.add_argument('--headless')
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
#
#     # def instantiation(self):
#
#
# # 每写完一个页面,都在main方法里面调用一下,确保没有问题再进行下一步.
# if __name__ == '__main__':
#     get = GetDriver()


# 实例化chrome浏览器
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# # 简单例子
# # 1、创建Chrome实例
# driver = webdriver.Chrome()
# # 2、driver.get方法将定位在给定的URL的网页
# driver.get("https://www.baidu.com/")  # get接受url可以是如何网址，此处以百度为例
# # 3、定位元素
# # 3.1、用id定位输入框对象
# driver.find_element(by=By.ID, value="kw").send_keys("python")
# # # 3.2、用id定位点击对象，用click()触发点击事件
# driver.find_element(by=By.ID, value="su").click()
#
# time.sleep(3)  # 延迟3秒
# # 4、退出访问的实例网站。
# driver.quit()


# 构建chrome实例
class GetDriver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
        # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 关闭被控制提示
        # options.add_argument("--no-sandbox")  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

        self.driver = webdriver.Chrome(options=options)
        # self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        # self.driver.add_experimental_option("excludeSwitches", ['enable-automation'])
        time.sleep(4)


if __name__ == '__main__':
    driver = GetDriver()
