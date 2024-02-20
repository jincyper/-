import unittest
from common.logining import Logining
from time import sleep
from selenium.webdriver.common.by import By


class OrderSearchPage(Logining):
    def order_num(self, number):
        self.driver.find_element(by=By.XPATH, value="//input[@class='ant-input']").send_keys(number)
        self.driver.find_element(by=By.XPATH, value="//button[@class='ant-btn ant-btn-primary']").click()
        sleep(2)

    def hand_num(self, handnumber):
        self.driver.find_element('xpath', "//input[@class='ant-input']").send_keys(handnumber)
        self.driver.find_element('xpath', "//button[@class='ant-btn ant-btn-primary']").click()
        sleep(2)

    def phone_num(self, phonenumber):
        self.driver.find_element('xpath', "//input[@class='ant-input']").send_keys(phonenumber)
        self.driver.find_element('xpath', "//button[@class='ant-btn ant-btn-primary']").click()
        sleep(2)

    def vip_name(self, vname):
        self.driver.find_element('xpath', "//input[@class='ant-input']").send_keys(vname)
        self.driver.find_element('xpath', "//button[@class='ant-btn ant-btn-primary']").click()
        sleep(2)

    # def order_empty(self):
    #     self.driver.find_element('xpath', "//button[@class='ant-btn']")
        # 通过收款方式(现金、微信记账、支付宝记账、美团点评、其他、会员卡)搜索订单数据
        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            0].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="现金"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            0].click()
        self.driver.find_element("xpath",
                                 '//div[@class="ant-select-item-option-content" and text()="微信记账"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            0].click()
        self.driver.find_element("xpath",
                                 '//div[@class="ant-select-item-option-content" and text()="支付宝记账"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            0].click()
        self.driver.find_element("xpath",
                                 '//div[@class="ant-select-item-option-content" and text()="美团点评"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            0].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="其他"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            0].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="会员卡"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        # 通过订单类型(开单、开卡、充值、卡变更)搜索订单数据
        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            1].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="开单"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            1].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="开卡"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            1].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="充值"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_elements("xpath", '//div[@class="ant-select ant-select-single ant-select-show-arrow"]')[
            1].click()
        self.driver.find_element("xpath", '//div[@class="ant-select-item-option-content" and text()="卡变更"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        # 通过下单时间(自定义[昨天到明天]、当天、近一个月、近三个月、近半年、近一年)搜索订单数据
        self.driver.find_element("xpath", '//span[@class="ant-calendar-picker"]').click()
        # 获取当前日期
        now = datetime.datetime.now()
        '''nowtime=str(now.year)+"年"+str(now.month)+"月"+str(now.day)+"日"
        print(nowtime)
        print(type(nowtime))'''
        # 获取昨天和明天的日期
        yesterday = (now + datetime.timedelta(days=-1)).strftime("%Y" + "年" + "%#m" + "月" + "%#d" + "日")
        tomorrow = (now + datetime.timedelta(days=1)).strftime("%Y" + "年" + "%#m" + "月" + "%#d" + "日")
        # 拼接元素路径
        Yday = '//td[@title="' + yesterday + '"]'
        Tday = '//td[@title="' + tomorrow + '"]'
        self.driver.find_element("xpath", Yday).click()
        self.driver.find_element("xpath", Tday).click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_element("xpath", '//span[@class="ant-calendar-picker"]').click()
        self.driver.find_element("xpath", '//span[@class="ant-tag ant-tag-blue" and text()="当天"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_element("xpath", '//span[@class="ant-calendar-picker"]').click()
        self.driver.find_element("xpath", '//span[@class="ant-tag ant-tag-blue" and text()="近一个月"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_element("xpath", '//span[@class="ant-calendar-picker"]').click()
        self.driver.find_element("xpath", '//span[@class="ant-tag ant-tag-blue" and text()="近三个月"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_element("xpath", '//span[@class="ant-calendar-picker"]').click()
        self.driver.find_element("xpath", '//span[@class="ant-tag ant-tag-blue" and text()="近半年"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        self.driver.find_element("xpath", '//span[@class="ant-calendar-picker"]').click()
        self.driver.find_element("xpath", '//span[@class="ant-tag ant-tag-blue" and text()="近一年"]').click()
        self.driver.find_element("xpath", '//button[@class="ant-btn ant-btn-primary"]').click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-btn"]').click()
        sleep(0.2)

        # 通过订单状态(待收款、已完成、已撤销)搜索订单数据
        self.driver.find_elements("xpath", '//label[@class="ant-radio-button-wrapper"]')[0].click()
        sleep(0.2)
        self.driver.find_elements("xpath", '//label[@class="ant-radio-button-wrapper"]')[1].click()
        sleep(0.2)
        self.driver.find_elements("xpath", '//label[@class="ant-radio-button-wrapper"]')[2].click()
        sleep(0.2)

        # 查看退款订单
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-link"]')[0].click()
        sleep(0.2)
        # 查看详情
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-link"]')[1].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-modal-close"]').click()
        sleep(0.2)
        # 打印小票
        self.driver.find_elements("xpath", '//button[@class="ant-btn ant-btn-link"]')[2].click()
        sleep(0.2)
        self.driver.find_element("xpath", '//button[@class="ant-modal-close"]').click()
        sleep(0.2)
        order = "*总部-收银-订单管理页面测试完成*\n"
        for o in order:
            sys.stdout.write(o)
            sys.stdout.flush()
            sleep(0.2)
        sleep(0.2)

    def order_search_check(self):
        try:
            txt = self.driver.find_element('xpath', "//div[@class='content-top']/div/span[6]").text
            sleep(1)
            # print(txt)
            return txt
        except Exception as e:
            print(e)
            return '搜索异常'

    def hand_search_check(self):
        try:
            txt = self.driver.find_element('xpath', "//div[@class='content-top']/div/span[7]/span[2]").text
            sleep(1)
            # print(txt)
            return txt
        except Exception as e:
            print(e)
            return '搜索异常'

    def phone_search_check(self):
        try:
            txt = self.driver.find_element('xpath', "//div[@class='member']/span[2]").text
            sleep(1)
            # print(txt)
            return txt
        except Exception as e:
            print(e)
            return '搜索异常'

    def vip_search_check(self):
        try:
            txt = self.driver.find_element('xpath', "//div[@class='member']/span[1]").text
            sleep(1)
            # print(txt)
            return txt
        except Exception as e:
            print(e)
            return '搜索异常'

    # def empty_search_check(self):
    #     try:
    #         txt = self.driver.find_elements('xpath', "//div[@class='content-top']/div/span[6]")
    #         # print(txt)
    #         return txt
    #     except Exception as e:
    #         print(e)
    #         return '搜索异常'

    def close(self):
        sleep(1)
        self.driver.quit()


if __name__ == "__main__":
    ordernum = OrderSearchPage()
    ordernum.order_num('2306081855510753003')
    print(ordernum.order_search_check())
    ordernum.close()

    orderhand = OrderSearchPage()
    orderhand.hand_num('11111aaaa')
    print(orderhand.hand_search_check())
    ordernum.close()

    orderphone = OrderSearchPage()
    orderphone.phone_num('15569955135')
    print(orderphone.phone_search_check())
    ordernum.close()

    ordervip = OrderSearchPage()
    ordervip.vip_name('朵天泽')
    print(ordervip.vip_search_check())
    ordernum.close()





