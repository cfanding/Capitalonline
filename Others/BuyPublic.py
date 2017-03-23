# -*- coding: utf-8 -*-
from __future__ import absolute_import
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from utils import GICTest


class BuyPublicTest(GICTest):
    """
        购买公网
    """
    def test_buy_public(self):
        url = 'http://101.251.234.165/zh-cn/cloud/wan/'
        self.login_into_page(url)

        # 购买/终止公网带宽
        buy_public_xpath = '/html/body/form/div[2]/div/div[2]/div[8]/a[2]'
        self.browser.find_element(By.XPATH, buy_public_xpath).click()

        # public bandwidth
        public_bandwidth_xpath = '/html/body/form/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/span'
        self.browser.find_element(By.XPATH, public_bandwidth_xpath).send_keys(Keys.RIGHT)

        # submit
        submit_xpath = '/html/body/form/div[2]/div[2]/div[7]/div[5]'
        self.browser.find_element(By.XPATH, submit_xpath).click()

        # confirm
        confirm_xpath = '/html/body/div[8]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, confirm_xpath).click()

        text = self.browser.switch_to.alert.text
        self.assertEqual(text, u'订单生成成功，资源任务正在执行,请等待,谢谢！')

if __name__ == '__main__':
    unittest.main()