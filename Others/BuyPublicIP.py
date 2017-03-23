# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from utils import GICTest


class BuyPublicIPTest(GICTest):
    """
        购买公网IP
    """
    def test_buy_public_ip(self):
        url = 'http://101.251.234.165/zh-cn/cloud/wan/'
        self.login_into_page(url)

        ip_link_xpath = '/html/body/form/div[2]/div/div[2]/div[12]/a'
        self.browser.find_element(By.XPATH, ip_link_xpath).click()

        # select ip
        ip_8_xpath = '/html/body/form/div[2]/div[2]/div[5]/div[2]/div/p[1]'
        self.browser.find_element(By.XPATH, ip_8_xpath).click()

        # submit
        submit_xpath = '/html/body/form/div[2]/div[2]/div[8]/div[5]'
        self.browser.find_element(By.XPATH, submit_xpath).click()

        # make sure
        yes_xpath = '/html/body/div[8]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, yes_xpath).click()

        text = self.browser.switch_to.alert.text
        self.assertEqual(text, u'订单生成成功，资源任务正在执行,请等待,谢谢！')

        self.browser.refresh()


if __name__ == '__main__':
    unittest.main()