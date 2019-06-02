#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/6/2 17:52
@file        : profilepage.py
@description : 个人中心界面
"""
from AppiumDemo.pageobject.pages.basepage import BasePage
from AppiumDemo.pageobject.pages.loginpage import LoginPage


class ProfilePage(BasePage):
    def gotoLogin(self):
        self.findByText("点击登录").click()
        return LoginPage()
