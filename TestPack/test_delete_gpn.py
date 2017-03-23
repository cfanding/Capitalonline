# -*- coding: utf-8 -*-
from __future__ import absolute_import
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.common.by import By
from GIC.utils import GICTest
from GIC import config


class DeleteGPN(GICTest):
    u"""删除GPN"""
    def test_delete_gpn(self):
        u"""删除GPN"""
        url = config.GPN_URL
        self.browser.get(url)

        # delete_gpn
        delete_gpn_xpath = '/html/body/form/div[2]/div/div[2]/input'
        self.browser.find_element(By.XPATH, delete_gpn_xpath).click()

        # 滑动条定位
        gpn_xpath = '/html/body/form/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/span'
        self.browser.find_element(By.XPATH, gpn_xpath).send_keys(Keys.LEFT)

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
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[6]").send_keys("7")
        self.browser.find_element(By.ID, 'id_buy_sub').click()

        # yes
        yes_xpath = '/html/body/div[7]/div[3]/div/button'
        self.browser.find_element(By.XPATH, yes_xpath).click()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(DeleteGPN("test_delete_gpn"))

    results = unittest.TextTestRunner().run(suite)