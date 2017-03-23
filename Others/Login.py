# -*- coding: utf-8 -*-
from __future__ import absolute_import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest

import config
# import KeyValue  # 导入函数


class LoginTest(unittest.TestCase):
    """用户注册 测试用例(feature)."""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.wait = WebDriverWait(self.browser, 30)
        self.browser.implicitly_wait(3)

    def test_login_success(self):
        """
        用户输入正确的用户名， 密码， 验证码， 能登录成功.

       """
        url = config.LOGIN_URL
        self.browser.get(url)
        # 输入正确的用户名
        self.browser.find_element(By.ID, "id_name").clear()
        self.browser.find_element(By.ID, "id_name").send_keys(config.USERNAME)

        # 输入正确的密码
        self.browser.find_element(By.ID, 'id_password_u').clear()
        self.browser.find_element(By.ID, 'id_password_u').send_keys(config.PASSWORD)

        try:
            self.browser.wait.until(lambda _driver: _driver.title == u'欢迎使用CDS云计算自服务平台')
            self.assertEqual(self.browser.title, u'欢迎使用CDS云计算自服务平台')
            print ("登录成功")
        except Exception, error:
            print (error, "登录失败")

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
