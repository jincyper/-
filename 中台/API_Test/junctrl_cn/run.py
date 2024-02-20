import unittest
# from HTMLTestRunnerPlugins import HTMLTestRunner
import HTMLTestRunner
import time

discover = unittest.defaultTestLoader.discover('case', '*test.py')

str_time = time.strftime('%Y%m%d_%H%M%S')  # 获取当前时间,并且格式为 年月日_时分秒
runner = HTMLTestRunner.HTMLTestRunner(stream=open(f'report/{str_time}测试报告.html', 'wb'), title='自动化测试报告',
                                       description='详细描述.')

# 执行
runner.run(discover)
