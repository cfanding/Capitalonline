# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class RegisterTest(unittest.TestCase):
    """用户注册 测试用例(feature)."""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.wait = WebDriverWait(self.browser, 10)
        self.browser.implicitly_wait(3)

    def test_register_success(self):
        """
        用户输入正确的用户名， 密码， 验证码， 能成功注册.
        """
        url = config.REGISTER_URL
        self.browser.get(url)

        # 清空已有数据
        # 输入正确的用户名
        self.browser.find_element(By.ID, 'id_mobile').clear()
        self.browser.find_element(By.ID, 'id_mobile').send_keys(config.USERNAME)

        # 输入正确的短信验证码
        self.browser.find_element(By.ID, 'id_checkCode').clear()
        self.browser.find_element(By.ID, 'id_checkCode').send_keys(config.SMS_CODE)

        # 输入正确的密码1
        self.browser.find_element(By.ID, 'id_password1').clear()
        self.browser.find_element(By.ID, 'id_password1').send_keys(config.PASSWORD)

        # 输入正确的密码2
        self.browser.find_element(By.ID, 'id_password2').clear()
        self.browser.find_element(By.ID, 'id_password2').send_keys(config.PASSWORD)

        # 同意“首都在线云自服务系统在线注册及首次登陆协议”协议
        _xpath = '//*[@id="customerForm"]/div[5]/div/div/label/input'
        self.browser.find_element(By.XPATH, _xpath).click()

        # 注册
        self.browser.find_element(By.ID, 'btnRegion').click()
        self.browser.wait.until(lambda _driver: _driver.find_element(By.TAG_NAME, 'body'))

        self.assertEqual(self.browser.title, u'用户注册完成')

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
