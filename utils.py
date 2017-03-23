# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from GIC import config

browser = webdriver.Firefox()


def setUpModule():
    global browser


def tearDownModule():
    global browser
    browser.quit()


class GICTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = browser
        cls.browser.wait = WebDriverWait(cls.browser, 30)
        cls.browser.implicitly_wait(3)

    # @classmethod
    # def tearDownClass(cls):
    #     cls.browser.quit()

    # def setUp(self):
    #     self.browser = browser
    #     self.browser.wait = WebDriverWait(self.browser, 30)
    #     self.browser.implicitly_wait(3)

    # def tearDown(self):
    #     self.browser.quit()

    def login_into_page(self, url):
        self.browser.get(url)
        # 输入正确的用户名
        self.browser.find_element(By.ID, "id_name").clear()
        self.browser.find_element(By.ID, "id_name").send_keys(config.USERNAME)

        # 输入正确的密码
        self.browser.find_element(By.ID, 'id_password_u').clear()
        self.browser.find_element(By.ID, 'id_password_u').send_keys(config.PASSWORD)

        # 验证当前网址和url是否一致
        self.browser.wait.until(lambda _driver: _driver.current_url == url)
        self.browser.maximize_window()

    @staticmethod
    def random_string(name_length):
        """随机生成一个指定长度的字符串.

        :param name_length:(int) specify length
        :return:
        """
        return ''.join(random.sample(string.ascii_letters, name_length))

