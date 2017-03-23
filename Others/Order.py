# -*- coding: utf-8 -*-

import unittest
from selenium.webdriver.common.by import By
from utils import GICTest
import config


class OrderTest(GICTest):
    """
        查询订单
    """
    def test_order(self):
        url = config.ORDER_URl
        # 登录
        self.login_into_page(url)

        # Account center
        self.browser.find_element(By.ID, "dh_account").click()

        # order
        self.browser.find_element(By.ID, "dh_account_order").click()


if __name__ == '__main__':
    unittest.main()