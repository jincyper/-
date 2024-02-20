import unittest
from common.logining import Logining
from time import sleep
from selenium.webdriver.common.by import By
import random


class MemberPage(Logining):
    def member_search(self):
        # 总部会员管理
        self.driver.find_element("xpath", '//li[@data-submenu-id="/member"]').click()
        sleep(0.2)
        # 进入门店会员页面
        self.driver.find_element("xpath", '//li[@data-menu-id="/member/store"]').click()
        sleep(0.2)
        # 会员搜索输入框输入会员姓名
        self.driver.find_element("xpath",
                                 '//input[@class="ant-input" and @placeholder="请输入会员姓名/手机号码后四位"]').send_keys(
            "泽")
        # 点击搜索按钮
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        # 点击会员详情按钮
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-link"]')[0].click()
        sleep(0.2)
        # 切换到舌诊记录
        self.driver.find_element("xpath", '//div[@class="ant-tabs-tab"]').click()
        sleep(0.2)
        # 选择并查看舌诊详情
        num = random.randint(0, 4)
        self.driver.find_elements("xpath", '//a[text()=" 详情 "]')[num].click()
        # 切换到舌诊对比
        self.driver.find_element("xpath", '//div[@class="list compare"]').click()
        sleep(0.2)
        # 点击历史记录框
        self.driver.find_element("xpath", '//span[@class="ant-select-selection-item"]').click()
        # 选择下拉列表选项
        self.driver.find_element("xpath",
                                 '//div[@class="ant-select-item-option-content" and text()="2022-09-19 14:58:58"]').click()
        sleep(0.2)
        member = "*总部-会员-门店会员页面测试完成*\n"
        for m in member:
            sys.stdout.write(m)
            sys.stdout.flush()
            sleep(0.2)
        sleep(0.2)
