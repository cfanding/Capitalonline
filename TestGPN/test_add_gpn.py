# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from GIC.utils import GICTest


class AddGPN(GICTest):
    """
        增加GPN
    """
    def test_add_gpn(self):
        u"""增加GPN"""
        url = 'http://101.251.234.165/zh-cn/cloud/gic/'
        self.browser.get(url)

        # 购买/终止GPN宽带
        self.browser.find_element(By.CLASS_NAME, "gongwang-goumai").click()

        # 滑动条
        gpn_xpath = '/html/body/form/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/span'
        self.browser.find_element(By.XPATH, gpn_xpath).send_keys(Keys.RIGHT)

        # confirm
        confirm_xpath = '/html/body/form/div[2]/div[2]/div[7]/div[5]'
        self.browser.find_element(By.XPATH, confirm_xpath).click()

        # confirm2
        confirm2_xpath = '/html/body/div[8]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, confirm2_xpath).click()

        text = self.browser.switch_to.alert.text
        self.assertEqual(text, u'GPN订单生成成功，资源任务正在执行,请等待,谢谢！')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(AddGPNTest("test_add_gpn"))

    results = unittest.TextTestRunner().run(suite)