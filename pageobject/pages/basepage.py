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
from selenium.webdriver.support.wait import WebDriverWait

from AppiumDemo.pageobject.drivers.androidclient import AndroidClient


class BasePage(object):
    def __init__(self):
        self._driver = AndroidClient.driver
        self.hw = self._driver.get_window_size()
        self.width = self.hw['width']
        self.height = self.hw['height']

    # 通用的查找方式
    def find(self, kv, timeout=10) -> WebElement:
        return WebDriverWait(self._driver, timeout).until(lambda x: x.find_element(*kv))

    def findByText(self, text) -> WebElement:
        return self.find((By.XPATH, "//*[@text='%s']" % text))

    def findById(self, resId) -> WebElement:
        return self.find((By.ID, "%s" % resId))

    def hasInfo(self, resId):
        page_source = self._driver.page_source
        print(page_source)
        return resId in page_source

    def swipeUp(self, sx=.5, sy=.9, ex=.5, ey=.1):
        self._driver.swipe(self.width*sx, self.height*sy, self.width*ex, self.height*ey)

    def swipeDown(self, sx=.5, sy=.1, ex=.5, ey=.9):
        self._driver.swipe(self.width*sx, self.height*sy, self.width*ex, self.height*ey)

    def getDisplayedHW(self):
        hw = self._driver.get_window_size()
        return hw["width"], hw["height"]
