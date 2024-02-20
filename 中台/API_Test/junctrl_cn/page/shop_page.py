import unittest
from common.logining import Logining
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ShopPage(Logining):
    def shop_set(self):
        # 总部店铺管理
        self.driver.find_element("xpath", '//li[@data-submenu-id="/shop"]').click()
        sleep(0.2)
        # 进入门店管理页面
        self.driver.find_element("xpath", '//li[@data-menu-id="/shop/list"]').click()
        sleep(0.2)
        # 搜索店铺
        self.driver.find_element("xpath", '//input[@placeholder="请输入..."]').send_keys("研发测试门店")
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        # 查看店铺详情
        self.driver.find_element("xpath", '//a[text()="查看"]').click()
        sleep(0.2)
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[1].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//a[text()=" 编辑 "]').click()
        sleep(0.2)
        # 获取负责电话
        phone = self.driver.find_elements("xpath", '//span[@id="address"]')[1].text
        # 全选并删除原有门店电话
        self.driver.find_element("xpath", '//input[@id="phonenumber"]').send_keys(Keys.CONTROL, "a")
        sleep(0.2)
        self.driver.find_element("xpath", '//input[@id="phonenumber"]').send_keys(Keys.BACKSPACE)
        # 将获取到的负责电话填入门店电话
        self.driver.find_element("xpath", '//input[@id="phonenumber"]').send_keys(phone)
        sleep(0.2)
        # 保存修改
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[1].click()
        sleep(0.2)
        # 重置搜索信息
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)