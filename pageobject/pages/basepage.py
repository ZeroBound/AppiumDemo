#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/25 15:27
@file        : basepage.py
@description : 所有 page 的父类
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from AppiumDemo.pageobject.drivers.androidclient import AndroidClient


class BasePage(object):
    def __init__(self):
        self._driver = AndroidClient.driver

    # 通用的查找方式
    def find(self, kv) -> WebElement:
        return self._driver.find_element(*kv)

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text=%s]" % text))
