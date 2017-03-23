# -*- coding: utf-8 -*-
import unittest
from selenium.webdriver.common.by import By
from utils import GICTest


class AlterEmail(GICTest):
    """更新email
    """

    def test_alter_email(self):
        url = 'http://101.251.234.165/zh-cn/account/to_protect/'
        self.login_into_page(url)

        # original_email
        value = self.browser.find_element(By.ID, "id_old_email_show").get_attribute('value')
        self.browser.find_element(By.ID, "id_old_email_show").clear()
        self.browser.find_element(By.ID, "id_old_email_show").send_keys(value)

        # new_email
        self.browser.find_element(By.ID, "id_new_email").send_keys(value)

        # verification code
        self.browser.find_element(By.CLASS_NAME, "anquanshezhi_lv").send_keys("222777")

        # update_email
        self.browser.find_element(By.CLASS_NAME, "chuangjian_lv").click()

        # 读取错误提示
        notice = self.browser.find_element(By.ID, 'id_new_email-error').text
        print notice


if __name__ == '__main__':
    unittest.main()
