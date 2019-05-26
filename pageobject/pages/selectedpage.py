#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/25 22:29
@file        : selectedpage.py
@description : 选择界面
"""
import time

from selenium.webdriver.common.by import By

from AppiumDemo.pageobject.pages.basepage import BasePage


class SelectedPage(BasePage):

    def isInSelectedPage(self):
        return False

    def gotoHuS(self):
        time.sleep(2)
        self.findByText("沪深").click()
        return self

    def getPriceName(self, name) -> float:
        price_locator = (By.XPATH,
                         "//*[contains(@resource-id, 'stockName') and @text='%s']/ancestor::*[3]"
                         "//*[contains(@resource-id, 'currentPrice')]" % name)
        price_text = self.find(price_locator).text
        return float(price_text)

    def getStockIndex(self, name) -> float:
        sz_stock = (By.XPATH,
                    "//*[contains(@resource-id, 'index_name') and @text='%s']"
                    "/preceding-sibling::*[1]" % name)
        stock_text = self.find(sz_stock).text
        return float(stock_text)
