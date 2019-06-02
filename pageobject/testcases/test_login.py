#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/6/2 18:12
@file        : test_login.py
@description : 测试登录
"""
import pytest

from AppiumDemo.pageobject.pages.app import App


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage = App.app_main().gotoProfile()

    def setup_method(self):
        self.loginPage = self.profilePage.gotoLogin()

    def teardown_method(self):
        self.loginPage.back()

    @pytest.mark.parametrize("user, pw, msg", [
        ("156005347600", "111111", "手机号码"),
        ("15600534760", "111111", "密码错误")
    ])
    def test_login_password(self, user, pw, msg):
        self.loginPage.loginByPassword(user, pw)
        assert msg in self.loginPage.getErrorMsg()
