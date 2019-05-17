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
wx_login_btn = "rl_login_by_wx"
other_login_btn = "tv_login_by_phone_or_others"
back_btn = "iv_action_back"


class TestClass(object):
    device = WebDriver
    @classmethod
    def setup_class(cls):
        print("pytest setup class")
        cls.device = init_driver()
        wait_element(cls.device, "user_profile_icon").click()

    def setup_method(self):
        print("pytest setup method")
        wait_element(self.device, "tv_login").click()

    def teardown_method(self):
        print("\npytest teardown method")
        # self.device.back()
        wait_element(self.device, back_btn).click()

    @classmethod
    def teardown_class(cls):
        print("pytest teardown class")
        cls.device.quit()

    @allure.story("手机号或邮箱登录")
    @pytest.mark.parametrize("username, password", [(17106576889, 1111), (10086, 123456), ("123456@qq.com", 123456)])
    def test_phone(self, username, password):
        login_more, login_acc, login_pwd = "login_more", "login_account", "login_password"
        login_next = "button_next"
        msg, ok_btn = "md_content", "md_buttonDefaultPositive"
        print("手机号或邮箱登录测试")
        wait_element(self.device, other_login_btn).click()
        wait_element(self.device, login_more).click()
        wait_element(self.device, login_acc).send_keys(username)
        wait_element(self.device, login_pwd).send_keys(password)
        wait_element(self.device, login_next).click()
        if wait_element(self.device, ok_btn).is_displayed():
            if "	请求太频繁，请稍后再试" == wait_element(self.device, msg).text:
                wait_element(self.device, ok_btn).click()
                return
            if len(str(username)) >= 13 or '@' in str(username):
                assert "用户名或密码错误" == wait_element(self.device, msg).text
            elif len(str(username)) < 13:
                assert "手机号码填写错误" == wait_element(self.device, msg).text
            wait_element(self.device, ok_btn).click()
        if "	请求太频繁，请稍后再试" == wait_element(self.device, msg).text:
            wait_element(self.device, ok_btn).click()


    @allure.story("微信登录")
    def test_weixin(self):
        print("微信登录测试")
        pass

    @allure.story("验证码登录")
    def test_verify_code(self):
        print("验证码登录测试")
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
