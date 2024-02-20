import unittest
from common.logining import Logining
from time import sleep
from selenium.webdriver.common.by import By


class EmployeeAddPage(Logining):
    def employee_add_click(self):
        # 总部员工管理
        self.driver.find_element("xpath", '//li[@data-submenu-id="/employee"]').click()
        sleep(1)
        # 进入员工角色页面
        self.driver.find_element("xpath", '//li[@data-menu-id="/employee/role"]').click()
        sleep(1)
        # 点击新增角色
        self.driver.find_element('xpath', "//button[@class='ant-btn ant-btn-primary active']").click()
        sleep(1)

    def employee_info(self, name):
        # 点击角色名称输入框并输入内容
        self.driver.find_element(by=By.XPATH, value="//input[@id='name']").send_keys(name)
        sleep(2)
        # 适用范围单选切换(区域通用)
        self.driver.find_elements("xpath", '//label[@class="ant-radio-wrapper"]')[1].click()
        sleep(2)
        # 适用范围单选切换(门店通用)
        self.driver.find_elements("xpath", '//label[@class="ant-radio-wrapper"]')[1].click()
        sleep(2)
        # 点击权限管理全选框
        self.driver.find_elements("xpath", '//label[@class="ant-checkbox-wrapper"]')[0].click()
        sleep(2)
        # 点击取消按钮
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(2)


        # 点击查看按钮(角色详情)
        self.driver.find_elements("xpath", '//a[text()="查看"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        # 点击编辑按钮(编辑角色)
        self.driver.find_elements("xpath", '//a[text()="编辑"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)
        # 点击删除按钮(删除角色)
        self.driver.find_elements("xpath", '//a[text()="删除"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-sm"]').click()
        sleep(0.2)

        # 进入员工账号页面
        self.driver.find_element("xpath", '//li[@data-menu-id="/employee/account"]').click()
        sleep(0.2)
        # 通过员工姓名查找员工
        self.driver.find_element("xpath", '//input[@placeholder="请输入员工姓名"]').send_keys("小朵")
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)
        # 通过员工编号查找员工
        self.driver.find_element("xpath", '//input[@placeholder="请输入员工编号"]').send_keys("JCtest001")
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)
        # 通过创建方查找员工
        self.driver.find_element("xpath", '//input[@class="ant-select-selection-search-input"]').send_keys("测试")
        self.driver.find_element("xpath", '//span[@title="研发测试门店"]').click()
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)
        # 点击新增员工账号按钮
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[1].click()
        sleep(0.2)
        self.driver.find_elements("xpath", '//button[@class="ant-btn"]')[1].click()
        sleep(0.2)
        # 查看已离职员工
        self.driver.find_element("xpath", '//a[text()="已离职员工"]').click()
        sleep(0.2)
        # 通过员工姓名搜索员工数据
        self.driver.find_elements("xpath", '//input[@class="ant-input"]')[0].send_keys("天泽")
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        # 通过员工编号搜索员工数据
        self.driver.find_elements("xpath", '//input[@class="ant-input"]')[1].send_keys("SHJK-027")
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)
        # 通过创建方搜索员工数据
        self.driver.find_element("xpath", '//input[@class="ant-select-selection-search-input"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//span[@title="钧控研发中心"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)



if __name__ == "__main__":
    employee = EmployeeAddPage()
    employee.employee_add_click()
    employee.employee_info('yi')
