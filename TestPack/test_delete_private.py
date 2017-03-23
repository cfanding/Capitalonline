# -*- coding: utf-8 -*-
# from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from GIC.utils import GICTest
from GIC import config


class DeletePrivate(GICTest):
    u"""删除私网"""
    def test_delete_priavte(self):
        u"""删除私网"""
        url = config.PRIVATE_URL
        self.browser.get(url)

        # adjust private
        adjust_private_xpath = '/html/body/div[6]/div/div[2]/table/tbody/tr[2]/td[6]/a'
        self.browser.find_element(By.XPATH, adjust_private_xpath).click()

        # delete_private
        self.browser.find_element(By.CLASS_NAME, 'goumaizhongzhi_del_network').click()

        # delete_confirm
        delete_confirm_xpath = '/html/body/div[8]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, delete_confirm_xpath).click()

        # notice
        notice_xpath = '/html/body/div[7]/div[3]/div/button'
        self.browser.find_element(By.XPATH, notice_xpath).click()

        print ("删除私网成功")


# 测试
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(DeletePrivate("test_delete_priavte"))

    results = unittest.TextTestRunner().run(suite)