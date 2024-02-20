import unittest
from common.logining import Logining
from time import sleep
from selenium.webdriver.common.by import By

class ItemCardPage(Logining):
    def item_search(self):
        # 总部品项卡管理
        self.driver.find_element("xpath", '//li[@data-submenu-id="/item"]').click()
        sleep(0.2)
        # 进入项目页面
        self.driver.find_element("xpath", '//li[@data-menu-id="/item/service"]').click()
        sleep(0.2)
        # 通过项目分组搜索项目数据
        self.driver.find_elements("xpath", '//div[@class="ant-select-selector"]')[0].click()
        self.driver.find_element("xpath", '//span[@title="九种体质推荐调理灸（钧控研发中心）"]').click()
        # 点击搜索按钮
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)
        # 通过创建来源搜索项目数据
        self.driver.find_element("xpath", '//span[@class="ant-select-selector"]').click()
        self.driver.find_elements("xpath", '//input[@class="ant-select-selection-search-input"]')[1].send_keys("测试")
        # self.driver.find_element("xpath",'//span[@class="ant-select-tree-title" and text()="研发测试门店"]').click()
        self.driver.find_element("xpath", '//span[@class="ant-select-tree-checkbox-inner"]').click()
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)
        # 通过项目名称/编号搜索项目数据
        self.driver.find_element("xpath", '//input[@class="ant-input"]').send_keys("实验")
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//input[@class="ant-input"]').clear()
        sleep(0.2)
        self.driver.find_element("xpath", '//input[@class="ant-input"]').send_keys("2")
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)
        # 通过项目状态搜索项目数据
        self.driver.find_elements("xpath", '//div[@class="ant-select-selector"]')[1].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="禁用"]').click()
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        self.driver.find_elements("xpath", '//div[@class="ant-select-selector"]')[1].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="启用"]').click()
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        # 点击新增项目按钮
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[1].click()
        sleep(0.2)
        # 输入项目名称(自动化测试项目)
        self.driver.find_element("xpath", '//input[@id="name"]').send_keys("自动化测试项目")
        sleep(0.2)
        # 点击新增分组
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-link"]').click()
        sleep(0.2)
        # 输入分组名称(自动化测试分组)
        self.driver.find_element("xpath", '//input[@id="form_in_modal_name"]').send_keys("自动化测试分组")
        sleep(0.2)
        # 点击保存按钮
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        # 选择项目分组
        self.driver.find_elements("xpath", '//span[@class="ant-select-selection-search"]')[0].click()
        sleep(0.2)
        self.driver.find_element("xpath",
                                 '//div[@class="ant-select-item-option-content" and text()="自动化测试分组(钧控研发中心)"]').click()
        sleep(0.2)
        # 选择适用门店
        self.driver.find_element("xpath", '//span[@class="ant-select-selector"]').click()
        self.driver.find_element("xpath", '//span[@class="ant-select-tree-checkbox-inner"]').click()
        sleep(0.2)
        # 输入门店价格
        self.driver.find_elements("xpath", '//input[@class="ant-input-number-input"]')[0].send_keys("100")
        sleep(0.2)
        self.driver.find_elements("xpath", '//input[@class="ant-input-number-input"]')[1].send_keys("90")
        sleep(0.2)
        self.driver.find_elements("xpath", '//input[@class="ant-input-number-input"]')[2].send_keys("50")
        self.driver.find_elements("xpath", '//input[@class="ant-input-number-input"]')[2].click()
        sleep(0.2)

        # 关联艾灸设备
        self.driver.find_element("xpath", '//span[text()="艾灸设备"]').click()
        sleep(0.2)
        # 拖动滚动条到指定目标元素
        targetChange1 = self.driver.find_element("xpath", '//textarea[@id="description"]')
        self.driver.execute_script("arguments[0].scrollIntoView()", targetChange1)
        sleep(0.2)
        # 点击添加按钮
        self.driver.find_element("xpath", '//span[text()="添 加"]').click()
        sleep(0.2)
        # 选择艾灸参数（选择悬停手法，穴位输入大椎并选择，修改时长）
        self.driver.find_elements("xpath", '//label[@class="ant-radio-button-wrapper"]')[1].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//li[text()="胸腹部"]').click()
        self.driver.find_element("xpath", '//span[text()="神阙穴"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//input[@id="inputNumber"]').send_keys(Keys.CONTROL, 'a')
        self.driver.find_element("xpath", '//input[@id="inputNumber"]').send_keys('45')
        sleep(0.2)
        # 点击确定按钮
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        # 选择适用体质（湿热）
        self.driver.find_element("xpath", '//input[@class="ant-checkbox-input" and @value="湿热"]').click()
        # 切换项目状态（禁用、启用）
        self.driver.find_element("xpath", '//span[text()="禁用"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//span[text()="启用"]').click()
        # 输入项目描述（自动化测试项目）
        text = "该项目为自动化测试创建,仅供自动化测试使用,请勿禁用、编辑、删除或使用该项目!\n" \
               "This project is created for automated test and is only used for automated test. Do not disable, edit, delete or use this project!\n"
        for t in text:
            self.driver.find_element("xpath", '//textarea[@id="description"]').send_keys(t)
            sleep(0.08)
        sleep(2)
        # 点击保存按钮
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary ant-btn-lg"]').click()
        sleep(0.2)
        # 搜索(自动化测试)项目
        self.driver.find_element("xpath", '//input[@class="ant-input"]').send_keys("自动化测试")
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-primary"]')[0].click()
        sleep(0.2)
        # 点击删除按钮
        self.driver.find_element("xpath", '//a[@class="del"]').click()
        sleep(0.2)
        # 二次确认
        self.driver.find_element("xpath", '//span[text()="是"]').click()
        sleep(0.2)
        # 点击分组管理
        self.driver.find_element("xpath", '//a[text()="分组管理"]').click()
        # 点击删除
        self.driver.find_elements("xpath", '//a[text()="删除"]')[-1].click()
        sleep(0.2)
        # 二次确认
        self.driver.find_element("xpath", '//span[text()="是"]').click()
        service = "*总部-品项卡-项目页面测试完成*\n"

        # 进入产品页面
        self.driver.find_element("xpath", '//li[@data-menu-id="/item/product"]').click()
        sleep(0.2)
        product = "*总部-品项卡-产品页面测试略…*\n"
        for p in product:
            sys.stdout.write(p)
            sys.stdout.flush()
            sleep(0.2)
        sleep(0.2)

        # 进入会员卡页面
        self.driver.find_element("xpath", '//li[@data-menu-id="/item/vipcard"]').click()
        sleep(0.2)
        # 点击新增会员卡模版
        self.driver.find_element("xpath", '//span[text()="新增会员卡模板"]').click()
        sleep(0.2)
        # 切换卡类型(次卡、折扣卡)
        self.driver.find_elements("xpath", '//label[@class="ant-radio-wrapper redio-card"]')[0].click()
        self.driver.find_elements("xpath", '//label[@class="ant-radio-wrapper redio-card"]')[1].click()
        sleep(0.2)
        # 输入卡名称
        self.driver.find_element("xpath", '//input[@id="name"]').send_keys("自动化测试折扣卡")
        # 选择可售卖门店
        self.driver.find_element("xpath", '//span[@class="ant-select-selector"]').click()
        self.driver.find_elements("xpath", '//span[@class="ant-select-tree-checkbox-inner"]')[0].click()
        self.driver.find_element("xpath", '//span[@class="ant-select-selector"]').click()
        sleep(0.2)
        # 选择可消费门店
        self.driver.find_elements("xpath", '//label[@class="ant-radio-wrapper"]')[0].click()
        self.driver.find_elements("xpath", '//label[@class="ant-radio-wrapper"]')[1].click()
        sleep(0.2)
        self.driver.find_elements("xpath", '//span[@class="ant-select-selector"]')[1].click()
        self.driver.find_elements("xpath", '//span[@class="ant-select-tree-checkbox-inner"]')[4].click()
        self.driver.find_elements("xpath", '//span[@class="ant-select-selection-item-content"]')[1].click()
        sleep(0.2)
        # 输入卡售价
        self.driver.find_element("xpath", '//input[@class="ant-input-number-input"]').send_keys("100")
        # 选择折扣范围
        self.driver.find_element("xpath", '//span[text()="全场通用"]').click()
        sleep(0.2)
        # 修改折扣值
        self.driver.find_element("xpath", '//input[@id="inputNumber"]').send_keys(Keys.CONTROL, 'a')
        self.driver.find_element("xpath", '//input[@id="inputNumber"]').send_keys("9")
        sleep(0.2)
        # 选择额外赠送项目
        self.driver.find_element("xpath", '//span[text()="赠送项目"]').click()
        # 拖动滚动条到指定目标元素
        targetChange2 = self.driver.find_element("xpath", '//textarea[@class="ant-input"]')
        self.driver.execute_script("arguments[0].scrollIntoView()", targetChange2)
        sleep(0.2)
        # 点击添加
        self.driver.find_element("xpath", '//span[@class="anticon anticon-plus"]').click()
        # 选择项目
        self.driver.find_element("xpath", '//span[text()="Test001"]').click()
        self.driver.find_element("xpath", '//input[@id="inputNumber"]').send_keys(Keys.ESCAPE)
        sleep(0.2)
        # 选择额外赠送产品
        self.driver.find_element("xpath", '//span[text()="赠送产品"]').click()
        # 拖动滚动条到指定目标元素
        targetChange3 = self.driver.find_element("xpath", '//textarea[@class="ant-input"]')
        self.driver.execute_script("arguments[0].scrollIntoView()", targetChange3)
        sleep(0.2)
        # 点击添加
        self.driver.find_elements("xpath", '//span[@class="anticon anticon-plus"]')[1].click()
        # 选择产品
        self.driver.find_element("xpath", '//span[text()="茯苓山楂益宁膏"]').click()
        sleep(0.2)
        # 选择有效期
        self.driver.find_element("xpath", '//span[text()="永久有效"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//span[text()="有效时间段"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//span[text()="有效天数"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//span[text()="从购买日起"]').click()
        sleep(0.2)
        # 修改会员卡有效天数
        self.driver.find_elements("xpath", '//input[@class="ant-input-number-input"]')[-1].send_keys(Keys.CONTROL, 'a')
        self.driver.find_elements("xpath", '//input[@class="ant-input-number-input"]')[-1].send_keys("10")
        sleep(0.2)
        # 输入说明
        text = "该折扣卡为自动化测试创建,仅供自动化测试使用,请勿禁用、编辑、删除或使用该会员卡!\n" \
               "This discount card is created for automated test only. Please do not disable, edit, delete or use this membership card!\n"
        for d in text:
            self.driver.find_element("xpath", '//textarea[@class="ant-input"]').send_keys(d)
            sleep(0.08)
        sleep(2)
        # 拖动滚动条到指定目标元素
        targetChange3 = self.driver.find_element("xpath", '//textarea[@class="ant-input"]')
        self.driver.execute_script("arguments[0].scrollIntoView()", targetChange3)
        sleep(0.2)
        # 点击取消按钮
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-lg"]').click()
        sleep(0.2)
        # 二次确认
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        vipcard = "*总部-品项卡-会员卡页面测试完成*\n"