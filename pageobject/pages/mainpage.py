#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/25 15:27
@file        : mainpage.py
@description : 主页面
"""
from selenium.webdriver.common.by import By

from AppiumDemo.pageobject.pages.basepage import BasePage
from AppiumDemo.pageobject.pages.searchpage import SearchPage


class MainPage(BasePage):
    def gotoOptional(self):
        self.findByText("自选")
        self.findByText("自选").click()

    def gotoSearch(self):
        search_btn = (By.ID, "home_search")
        self.find(search_btn).click()
        return SearchPage()
