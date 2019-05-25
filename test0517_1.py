#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/19 21:13
@file        : test0517_1.py
@description : 基金开户 蛋卷已有账户登录 密码登陆 输入错误的用户名和密码，点击安全登陆
"""
import os
import time

import pytest
from appium import webdriver
# from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
# from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestFundWebView(object):
    device = WebDriver
    @classmethod
    def setup_class(cls):
        cls.device = init_driver()
        print("setup------class")
        print(cls.device.contexts)

    def setup_method(self):
        transaction_btn = "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='交易']"
        print("setup------method1")
        print(self.device.contexts)
        wait_xpath_element(self.device, transaction_btn, msg='交易按钮').click()
        print("setup------method2")
        print(self.device.contexts)
        print("setup------method-----end")

    def teardown_method(self):
        if wait_id_element(self.device, "android:id/message", msg='弹框信息').is_displayed():
            wait_id_element(self.device, "android:id/button1", msg='点击确定').click()

    @classmethod
    def teardown_class(cls):
        cls.device.quit()

    @pytest.mark.parametrize("tel, pwd", [(13778786985, 123456)])
    def test_fund_view(self, tel, pwd):
        device = self.device
        fund_open = "//android.view.View[@content-desc='基金开户']"
        use_pwd = "//android.view.View[@content-desc='使用密码登录']"
        sec_login = "//android.widget.Button[@content-desc='安全登录']"
        wait_xpath_element(device, fund_open, msg="基金开户")
        time.sleep(5)
        print("基金开户")
        device.find_element_by_accessibility_id("基金开户").click()
        device.find_element_by_accessibility_id("已有蛋卷基金账户登录").click()
        time.sleep(5)
        wait_xpath_element(device, use_pwd, msg='使用密码登录按钮').click()
        wait_id_element(device, "telno", msg='输入手机号').send_keys(tel)
        wait_id_element(device, "pass", msg='输入密码').send_keys(pwd)
        wait_xpath_element(device, sec_login, msg="安全登录").click()
        msg = wait_id_element(device, "android:id/message", msg='弹框信息').text
        assert "你输入的手机号码或者密码有误" in msg


# 初始化
def init_driver() -> WebDriver:
    caps = {
        "platformName": "Android",
        "deviceName": "XiaoMi",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "autoGrantPermissions": True,
        "unicodeKeyboard": True,
        "resetKeyboard": False,
        "noReset": True
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(20)
    return driver


def wait_xpath_element(driver: WebDriver, xpath, timeout=10, msg='') -> WebElement:
    # WebDriverWait(driver, timeout).until(lambda x: x.find_element_by_xpath(xpath))
    method = EC.presence_of_element_located((By.XPATH, xpath))
    # method = EC.presence_of_all_elements_located((By.XPATH, xpath))
    if msg:
        msg = "{0}s 内没有找到{1}元素".format(timeout, msg)
    else:
        msg = "没有找到元素"
    return WebDriverWait(driver, timeout).until(method, message=msg)


def wait_id_element(driver: WebDriver, resid, timeout=10, msg='') -> WebElement:
    # WebDriverWait(driver, timeout).until(lambda x: x.find_element_by_xpath(xpath))
    method = EC.presence_of_element_located((By.ID, resid))
    # method = EC.presence_of_all_elements_located((By.XPATH, xpath))
    if msg:
        msg = "{0}s 内没有找到\"{1}\"元素".format(timeout, msg)
    else:
        msg = "没有找到元素"
    return WebDriverWait(driver, timeout).until(method, message=msg)


if __name__ == "__main__":
    cur_file = os.path.basename(__file__)
    pytest.main([cur_file])
