# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utils import GICTest


class DeletePublicIPTest(GICTest):
    """

    """
    def test_delete_public_ip(self):
        url = 'http://101.251.234.165/zh-cn/cloud/wan/'
        self.login_into_page(url)

        ip_link_xpath = '/html/body/form/div[2]/div/div[2]/div[12]/a'
        self.browser.find_element(By.XPATH, ip_link_xpath).click()

        # delete ip
        ip_xpath = '/html/body/form/div[2]/div[2]/div[3]/div[2]/div/div'
        self.browser.find_element(By.XPATH, ip_xpath).click()

        # make sure
        yes_xpath = '/html/body/div[8]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, yes_xpath).click()

        # send SMS
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[1]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[2]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[3]").send_keys("2")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[4]").send_keys("7")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[5]").send_keys("7")
        self.browser.find_element(By.XPATH, "/html/body/form/div[4]/center/input[6]").send_keys("7")
        self.browser.find_element(By.ID, 'id_buy_sub').click()
        self.browser.wait.until(lambda _driver: _driver.find_element(By.ID, 'AlertMessageBody').text != '')
        text = self.browser.find_element(By.ID, 'AlertMessageBody').text
        self.assertEqual(text, u'删除网段任务已经提交，等待执行！')


if __name__ == '__main__':
    unittest.main()
