import unittest
from page.login_page import LoginPage


class LoginCase(unittest.TestCase):
    def setUp(self):
        self.login = LoginPage()
        self.login.open()

    def test_login_success(self):   # 登录成功
        self.login.login('agenttest', 'agenttest123')    # 正确的账号密码
        result = self.login.login_check()   # 返回True
        # print("1", result)
        self.assertTrue(result )

    def test_login_error(self):  # 登录失败
        self.login.login('agent', 'agent123')  # 错误的密码
        result = self.login.login_check()   # 返回False
        # print("2", result)
        self.assertFalse(result)

    def tearDown(self):
        self.login.close()


if __name__ == '__main__':
    unittest.main()

