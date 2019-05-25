#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/25 15:26
@file        : androidclient.py
@description : 驱动类
"""
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):
    # driver: WebDriver
    @classmethod
    def init_driver(cls) -> WebDriver:
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
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(20)
        return cls.driver
