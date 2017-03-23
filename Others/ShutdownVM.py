# -*- coding: utf-8 -*-
# from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from utils import GICTest


class ShutdownVMTest(GICTest):
    """
        关闭虚拟机
    """
    def test_shutdown_vm(self):
        url = 'http://101.251.234.165/zh-cn/cloud/vm/'
        self.login_into_page(url)

        # More operations
        more_operations_xpath = '/html/body/form/div[2]/div/div[2]/table/tbody/tr[2]/td[8]/span'
        self.browser.find_element(By.XPATH, more_operations_xpath).click()

        # Shutdown_vm
        shutdown_xm_xpath = '/html/body/form/div[2]/div/div[2]/table/tbody/tr[2]/td[8]/div/div[2]'
        self.browser.find_element(By.XPATH, shutdown_xm_xpath).click()


if __name__ == '__main__':
    unittest.main()



