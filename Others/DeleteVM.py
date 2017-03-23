# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By

from utils import GICTest


class DeleteVMTest(GICTest):
    """
        删除虚拟机
    """
    def test_delete_vm(self):
        url = 'http://101.251.234.165/zh-cn/cloud/vm/'
        # login
        self.login_into_page(url)
        # 删除云主机
        select_xpath = '/html/body/form/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/span'
        self.browser.find_element(By.XPATH, select_xpath).click()
        delete_xpath = '/html/body/form/div[2]/div/div[2]/table/tbody/tr[1]/td[8]/div/div[3]'
        self.browser.find_element(By.XPATH, delete_xpath).click()

        # makesure
        yes_xpath = '/html/body/div[9]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, yes_xpath).click()

        # send SMS
        self.browser.find_element(By.XPATH, "/html/body/div[5]/center/input[1]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/div[5]/center/input[2]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/div[5]/center/input[3]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/div[5]/center/input[4]").send_keys("7")
        self.browser.find_element(By.XPATH, "/html/body/div[5]/center/input[5]").send_keys("7")
        self.browser.find_element(By.XPATH, "/html/body/div[5]/center/input[6]").send_keys("7")
        self.browser.find_element(By.ID, 'id_buy_sub').click()

        text = self.browser.find_element(By.ID, 'AlertMessageBody').text
        self.assertEqual(text, u'删除云主机已成功提交，等待执行！')


if __name__ == '__main__':
    unittest.main()
