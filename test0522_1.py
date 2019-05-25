#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/22 21:38
@file        : test0522_1.py
@description : 
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


class TestWebView(object):
    device = WebDriver
    @classmethod
    def setup_class(cls):
        cls.device = init_driver()
        print("setup------class")
        print(cls.device.contexts)

    def setup_method(self):
        action_more = "com.android.browser:id/action_more"
        action_home = "com.android.browser:id/action_home"
        print("setup------method1")
        wait_id_element(self.device, action_home).click()
        print(self.device.contexts)
        print("setup------method-----end")

    def teardown_method(self):
        pass

    @classmethod
    def teardown_class(cls):
        cls.device.quit()

    def test_browser_view(self):
        device = self.device
        print("\ntest_browser_view==========")
        print(device.contexts)
        print("=============================")
        # 版本对应关系
        # https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md
        # 一、未设置 chromedriverExecutableDir 前报错, 默认 ChromeDriver 2.46.628402
        # No Chromedriver found that can automate Chrome '57.0.2987'
        # 二、设置 ChromeDriver 为 2.34 还是报上述错误
        # 三、设置 ChromeDriver 为 2.28 出现如下错误
        # 在这切换的时候卡着不动
        # [Chromedriver] Error: Failed to start Chromedriver session:
        # An unknown server-side error occurred while processing the command.
        # Original error: chrome not reachable
        # chrome driver 2.29
        # SystemWebView 57.0.2987.132(adb shell dumpsys package com.google.android.webview)
        # chrome://inspect 显示 com.android.browser (61.0.3163.128)
        device.switch_to.context(device.contexts[1])
        print(device.contexts)
        time.sleep(10)


# 初始化
def init_driver() -> WebDriver:
    caps = {
        "platformName": "Android",
        "deviceName": "XiaoMi",
        "appPackage": "com.android.browser",
        "appActivity": ".BrowserActivity",
        "autoGrantPermissions": True,
        "unicodeKeyboard": True,
        "resetKeyboard": False,
        "noReset": True,
        "chromedriverExecutableDir": "F:\\BrowserDownloads\\chromedriver_win32\\2.28"
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
