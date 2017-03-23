# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from GIC.utils import GICTest
from GIC import config


class CreateVM(GICTest):
    u"""创建虚拟机"""
    def test_create_vm(self):
        u"""创建虚拟机"""
        url = config.VM_URL
        # 登录
        self.browser.get(url)

        # click create VM
        create_xpath = '/html/body/form/div[2]/div/div[1]/input'
        self.browser.find_element(By.XPATH, create_xpath).click()
        self.browser.find_element(By.ID, "id_vm_name").send_keys(self.random_string(4))
        self.browser.find_element(By.ID, "id_vm_number").send_keys("123")
        self.browser.find_element(By.ID, "id_vm_password").send_keys("november24,")
        self.browser.find_element(By.ID, "id_vm_password_confirm").send_keys("november24,")

        # select cpu
        cpu_xpath = '/html/body/form/div[2]/div[2]/div[7]/table/tbody/tr/td[2]/div/p[3]'
        self.browser.find_element(By.XPATH, cpu_xpath).click()
        # select ram
        ram_xpath = '/html/body/form/div[2]/div[2]/div[8]/table/tbody/tr/td[2]/div/p[3]'
        self.browser.find_element(By.XPATH, ram_xpath).click()
        # select os
        os_type_xpath = '/html/body/form/div[2]/div[2]/div[13]/div[2]/div[1]/p[4]'
        self.browser.find_element(By.XPATH, os_type_xpath).click()
        os_xpath = '/html/body/form/div[2]/div[2]/div[13]/div[2]/div[3]/div[4]/select/option[4]'
        self.browser.find_element(By.XPATH, os_xpath).click()
        # select networkd, just private network
        private_network_xpath = '/html/body/form/div[2]/div[2]/div[16]/div[2]/div[1]/div/span/input'
        self.browser.find_element(By.XPATH, private_network_xpath).click()

        # select vm count.
        # self.browser.find_element(By.ID, "vm_num").clear()
        # self.browser.find_element(By.ID, "vm_num").send_keys("1")

        # submit
        self.browser.find_element(By.ID, "ok").click()
        # make sure
        yes_xpath = '/html/body/div[9]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, yes_xpath).click()

        text = self.browser.switch_to.alert.text
        self.assertEqual(text, u'购买成功，等待任务执行！')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CreateVM("test_create_vm"))

    results = unittest.TextTestRunner().run(suite)
