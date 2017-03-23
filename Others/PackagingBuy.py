# -*- coding: utf-8 -*-
from __future__ import absolute_import
import unittest
from selenium.webdriver.common.by import By

from utils import GICTest


class PackageBuyTest(GICTest):
    """用户注册 测试用例(feature)."""

    def test_package_buy_success(self):
        """正确的信息， 能够成功打包购买云主机.

        """
        # url = 'http://101.251.234.165/zh-cn/shop/buy/guide'
        # 登录
        self.login_into_page()

        # 输入正确的名称
        app = self.browser.find_element(By.ID, 'id_app_name')
        app.clear()
        app.send_keys(self.random_string(3))

        # 选择国家
        china_xpath = '/html/body/form/div[2]/div/div[2]/div[1]/div[9]/div[2]/div[1]/p[1]'
        self.browser.find_element(By.XPATH, china_xpath).click()

        # 选择数据中心
        beijing_xpath = '/html/body/form/div[2]/div/div[2]/div[1]/div[9]/div[2]/div[2]/p'
        tag_p = self.browser.wait.until(lambda _driver: _driver.find_element(By.XPATH, beijing_xpath))
        tag_p.click()

        # next step
        self.browser.find_element(By.ID, 'id_guide1_next').click()

        # select pipe
        pipe_xpath = '/html/body/form/div[2]/div/div[2]/div[2]/div[5]/span/p[1]'
        self.browser.find_element(By.XPATH, pipe_xpath).click()

        # select ip
        ip_xpath = '/html/body/form/div[2]/div/div[2]/div[2]/div[7]/p[1]'
        self.browser.find_element(By.XPATH, ip_xpath).click()

        # select LAN
        self.browser.find_element(By.ID, "id_lan1_net_id").send_keys("192.168.1.0")
        self.browser.find_element(By.ID, "id_lan1_mask").clear()
        self.browser.find_element(By.ID, "id_lan1_mask").send_keys("24")

        # next step
        self.browser.find_element(By.ID, "id_guide2_next").click()

        # # create vm
        # 输入正确的主机名
        self.browser.find_element(By.ID, "id_vm_name").send_keys('host_name')
        # 输入正确的密码
        self.browser.find_element(By.ID, "id_vm_password").send_keys("november24,.")
        # 重复正确的密码
        self.browser.find_element(By.ID, "id_vm_password_confirm").send_keys("november24,.")
        # 选择CPU
        cpu_xpath = '/html/body/form/div[2]/div/div[2]/div[3]/div[13]/span/p[1]'
        self.browser.find_element(By.XPATH, cpu_xpath).click()
        # 选择RAM
        ram_xpath = '/html/body/form/div[2]/div/div[2]/div[3]/div[14]/table/tbody/tr/td[2]/div/p[1]'
        self.browser.find_element(By.XPATH, ram_xpath).click()
        # 选择操作系统
        os_type_xpath = '/html/body/form/div[2]/div/div[2]/div[3]/div[18]/div[2]/div[1]/p[4]'
        self.browser.find_element(By.XPATH, os_type_xpath).click()
        os_xpath = '/html/body/form/div[2]/div/div[2]/div[3]/div[18]/div[2]/div[3]/div[4]/select/option[4]'
        self.browser.find_element(By.XPATH, os_xpath).click()

        # submit
        self.browser.find_element(By.ID, "id_guide3_next").click()

        # 确认购买
        sure_xpath = '/html/body/div[8]/div[3]/div/button[1]'
        self.browser.find_element(By.XPATH, sure_xpath).click()
        text = self.browser.switch_to.alert.text

        self.assertEqual(text, u'订单生成成功，资源任务正在执行,请等待,谢谢！')


if __name__ == '__main__':
    unittest.main()
