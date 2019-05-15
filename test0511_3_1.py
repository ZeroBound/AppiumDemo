#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/14 22:05
@file        : test0511_3.py.py
@description :
完成雪球登录场景的测试
要求带有setup_class setup_method体系
微信 验证码 密码 错误的用户名 错误的密码 至少编写5条用例
"""
import os

import allure
import pytest
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

# id
user_icon = "user_profile_icon"
login_btn = "tv_login"
wx_login_btn = "rl_login_by_wx"
other_login_btn = "tv_login_by_phone_or_others"


class TestClass(object):
    device = WebDriver
    @classmethod
    def setup_class(cls):
        print("pytest setup class")
        cls.device = init_driver()
        wait_element(cls.device, user_icon).click()

    def setup_method(self):
        print("pytest setup method")
        wait_element(self.device, login_btn).click()

    def teardown_method(self):
        print("\npytest teardown method")
        self.device.back()

    @classmethod
    def teardown_class(cls):
        print("pytest teardown class")
        cls.device.quit()

    @allure.story("手机号登录")
    @pytest.mark.parametrize("username, password", [(17106576889, 1111), (10086, 123456)])
    def test_phone(self, username, password):
        pass

    @allure.story("邮箱登录")
    def test_email(self, email, password):
        pass

    @allure.story("微信登录")
    def test_weixin(self):
        pass

    @allure.story("验证码登录")
    def test_verify_code(self):
        pass


# 初始化
def init_driver() -> WebDriver:
    caps = {
        "platformName": "android",
        "deviceName": "XiaoMi",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "autoGrantPermissions": True,
        "unicodeKeyboard": True,
        "noReset": True
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    driver.implicitly_wait(20)
    return driver


def wait_element(driver: WebDriver, resid, timeout=10) -> WebElement:
    return WebDriverWait(driver, timeout).until(lambda x: x.find_element_by_id(resid))


if __name__ == "__main__":
    test_file = os.path.basename(__file__)
    pytest.main(['-s', '-v', test_file])
