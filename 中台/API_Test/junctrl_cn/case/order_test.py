import unittest
from page.order_page import OrderSearchPage


class OrderSearchTest(unittest.TestCase):
    def Setup(self):
        self.order = OrderSearchPage()

    def tearDown(self):
        self.order.close()

    def test_search_success(self):
        self.order.order_num('2306081855510753003')
        result = self.order.order_search_check()
        self.assertEqual(result, '2306081855510753003')

    def test_hand_num_search_success(self):
        self.order.hand_num('11111aaaa')
        result = self.order.hand_search_check()
        self.assertEqual(result, '11111aaaa')

    def test_phone_num_search_success(self):
        self.order.phone_num('15569955135')
        result = self.order.phone_search_check()
        self.assertEqual(result, '15569955135')

    def test_vip_name_search_success(self):
        self.order.vip_name('朵天泽')
        result = self.order.vip_search_check()
        self.assertEqual(result, '朵天泽')




if __name__ == '__main__':
    unittest.main()
