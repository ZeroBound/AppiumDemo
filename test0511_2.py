#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/13 21:37
@file        : test0511_2.py
@description :
进入雪球首页，
进入基金的新闻页（不是第一个基金按钮），
对他以及它右侧的每个新闻栏目，
执行上滑5次，进入下个栏目用从右边到左边滑动
滑动使用相对坐标，而不是绝对坐标
"""
import time
import unittest

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class TestExerciseTwo(unittest.TestCase):
    caps = {
        "platformName": "android",
        "deviceName": "XiaoMi",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "autoGrantPermissions": True,
        "unicodeKeyboard": True,
        "noReset": True
    }

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", TestExerciseTwo.caps)
        cls.driver.implicitly_wait(20)
        print("set up class ")

    def setUp(self):
        print("set up")

    def tearDown(self):
        self.driver.quit()
        print("tear down")

    @classmethod
    def tearDownClass(cls):
        print("tear down class")

    def test_two(self):
        device = self.driver
        size = device.get_window_size()
        h, w = size['height'], size['width']

        btn_contain = "//*[contains(@resource-id, 'buttons_container')]"
        fund = "//*[contains(@resource-id, 'indicator')]//*[@text='基金']"

        wait_xpath_element(device, btn_contain)
        wait_xpath_element(device, fund).click()
        self.assertTrue('基金' == get_cur_tab_page(device).text, "基金未被选中状态")

        tabs = get_new_tabs(device)
        time.sleep(10)
        if '基金' in tabs:
            tabs = tabs[tabs.index('基金')+1::]
        for tab in tabs:
            swipe_up(device, w/2, h*0.8, w/2, h*0.3, num=5)
            # 从右往左滑
            device.swipe(w*0.9, h/2, w*0.1, h/2)
            actual = get_cur_tab_page(device).text
            print("预期: %s ---->实际: %s " % (tab, actual))
            self.assertEqual(tab, actual, "滑动后与实际显示不一致")


# 等待 xpath 元素点击
def wait_xpath_element(driver: WebDriver, xpath, timeout=10) -> WebElement:
    wl = WebDriverWait(driver, timeout).until(lambda x: x.find_element_by_xpath(xpath))
    # print(wl)
    return wl


# 获取新闻信息的 Tab 标签值
def get_new_tabs(driver: WebDriver):
    text_view = "//*[contains(@resource-id, 'indicator')]//*[@class='android.widget.TextView']"
    new_tabs = driver.find_element_by_id("indicator")
    # {'height': 60, 'width': 720, 'x': 0, 'y': 221}
    # 获取 tabs 标签的 rect
    rect = new_tabs.rect
    tab_h = rect['y'] + rect['height']/2
    tab_w = rect['width']
    # 获取 tab 的所有 text 值
    before_text = [b.text for b in driver.find_elements_by_xpath(text_view)]
    # print(before_text)
    driver.swipe(tab_w*.9, tab_h, tab_w*.2, tab_h)
    time.sleep(2)
    after_text = [a.text for a in driver.find_elements_by_xpath(text_view)]
    # print(after_text)
    driver.swipe(tab_w*.2, tab_h, tab_w*.9, tab_h)
    time.sleep(1)
    for i in before_text:
        if i in after_text:
            after_text.remove(i)
    before_text.extend(after_text)
    return before_text


# 获取当前 Tab 标签页的值
def get_cur_tab_page(driver: WebDriver):
    # 当前新闻页 tab 的标签
    # cur_focus = "//*[contains(@resource-id, 'indicator')]//*[@class='android.view.View']"
    cur_focus_tab = "//*[contains(@resource-id, 'indicator')]//*[@class='android.view.View']/" \
                    "preceding-sibling::android.widget.TextView"
    tab, wait_time = '', 20
    try:
        time.sleep(10)
        tab = wait_xpath_element(driver, cur_focus_tab, timeout=wait_time)
    except TimeoutException:
        print("%ds 内未找到当前选中的新闻页标签" % wait_time)
    except NoSuchElementException:
        print("未找到当前选中的新闻页标签")
    return tab


# 上滑操作
def swipe_up(driver: WebDriver, sx, sy, ex, ey, num=1):
    for i in range(num):
        # 从下往上滑
        driver.swipe(sx, sy, ex, ey)
        time.sleep(2)
    time.sleep(1)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestExerciseTwo))
    unittest.TextTestRunner(verbosity=2).run(suite)
