# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils import GICTest


class NetworkdBuy(GICTest):
    """输入正确， 购买网络成功.

    """
    def test_network_buy(self):
        url = 'http://101.251.234.165/zh-cn/cloud/wan/'
        self.login_into_page(url)

        link_xpath = '/html/body/form/div[2]/div/div[2]/div[8]/a[2]'
        self.browser.find_element(By.XPATH, link_xpath).click()

        # adjust bandwidth
        bandwidth_xpath = '/html/body/form/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/span'
        self.browser.find_element(By.XPATH, bandwidth_xpath).send_keys(Keys.RIGHT)

        # submit
        submit_xpath = '/html/body/form/div[2]/div[2]/div[7]/div[5]'
        self.browser.find_element(By.XPATH, submit_xpath).click()
        # make sure
        yes_xpath = '/html/body/div[8]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, yes_xpath).click()

        text = self.browser.switch_to.alert.text
        self.assertEqual(text, u'订单生成成功，资源任务正在执行,请等待,谢谢！')


if __name__ == '__main__':
    unittest.main()