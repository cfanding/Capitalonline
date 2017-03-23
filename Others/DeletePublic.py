# -*- coding: utf-8 -*-
from __future__ import absolute_import
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from utils import GICTest


class DeletePublicTest(GICTest):
    """
        删除公网
    """
    def test_delete_public(self):
        url = 'http://101.251.234.165/zh-cn/cloud/wan/'
        self.login_into_page(url)

        delete_public_xpath = '/html/body/form/div[2]/div/div[2]/div[8]/a[2]'
        self.browser.find_element(By.XPATH, delete_public_xpath).click()

        # public bandwidth
        public_bandwidth_xpath = '/html/body/form/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/span'
        self.browser.find_element(By.XPATH, public_bandwidth_xpath).send_keys(Keys.LEFT)

        # confirm
        confirm_xpath = '/html/body/form/div[2]/div[2]/div[7]/div[5]'
        self.browser.find_element(By.XPATH, confirm_xpath).click()

        # confirm2
        confirm2_xpath = '/html/body/div[8]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, confirm2_xpath).click()

        # send SMS
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[1]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[2]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[3]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[4]").send_keys("7")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[5]").send_keys("7")
        self.browser.find_element(By.ID, 'id_buy_sub').click()

        # confirm3
        confirm3_xpath = '/html/body/div[7]/div[3]/div/button'
        self.browser.find_element(By.XPATH, confirm3_xpath).click()


# 测试
if __name__ == '__main__':
    unittest.main()




