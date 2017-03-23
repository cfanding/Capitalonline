# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By
from GIC.utils import GICTest
import time
import GIC.config
import os


class InformationTest(GICTest):
    """
    完善信息
    """
    def test_information(self):
        url = GIC.config.INFORMATION_URL
        self.login_into_page(url)

        # 公司名称
        time.sleep(3)
        self.browser.find_element(By.NAME, "company_name").clear()
        self.browser.find_element(By.NAME, "company_name").send_keys(self.random_string(4))
        # 办公地址
        self.browser.find_element(By.ID, 'P1').click()
        self.browser.find_element_by_xpath("//option[@value='2']").click()
        self.browser.find_element(By.ID, 'C1').click()
        self.browser.find_element_by_xpath("//option[@value='382']").click()
        self.browser.find_element_by_name("work_address").clear()
        self.browser.find_element_by_name("work_address").send_keys(u"首都在线")
        # 注册地址
        self.browser.find_element(By.ID, 'P2').click()
        self.browser.find_element_by_xpath("//option[@value='2']").click()
        self.browser.find_element(By.ID, 'C1').click()
        self.browser.find_element_by_xpath("//option[@value='382']").click()
        self.browser.find_element_by_name("register_address").clear()
        self.browser.find_element_by_name("register_address").send_keys(u"首都在线")
        # 主联系人
        time.sleep(3)
        self.browser.find_element_by_name("contact_name").clear()
        self.browser.find_element_by_name("contact_name").send_keys("18678675566")
        # 手机号
        time.sleep(2)
        self.browser.find_element_by_name("mobile").clear()
        self.browser.find_element_by_name("mobile").send_keys("18678675566")
        # 邮箱地址
        time.sleep(2)
        self.browser.find_element_by_name("email").clear()
        self.browser.find_element_by_name("email").send_keys("18678675566@qq.com")
        # 验证码
        self.browser.find_element_by_name("mobile_checkcode").send_keys("222777")
        # 营业执照正本
        self.browser.find_element_by_id("up_imgFile_yyzz").click()
        os.system("D:\\abc\\apfile.exe")
        time.sleep(2)
        # 营业执照副本
        self.browser.find_element_by_id("up_imgFile_yyzzt").click()
        os.system("D:\\abc\\apfile.exe")
        time.sleep(2)
        # 提交
        self.browser.find_element_by_xpath("//input[@value='提交']").click()
        # 关闭提示信息
        buttons = self.browser.find_element_by_class_name('modal-header').find_elements_by_tag_name('button')
        text = self.browser.find_element_by_class_name('modal-title').text
        self.assertEqual(text, u'提示信息')
        buttons[0].click()

# 测试
if __name__ == '__main__':
    unittest.main()





