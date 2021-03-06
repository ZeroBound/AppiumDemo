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
from AppiumDemo.pageobject.pages.profilepage import ProfilePage
from AppiumDemo.pageobject.pages.searchpage import SearchPage
from AppiumDemo.pageobject.pages.selectedpage import SelectedPage


class MainPage(BasePage):
    _profile_button = (By.ID, "user_profile_icon")
    _search_button = (By.ID, "home_search")

    def isInMainPage(self):
        pass

    def gotoOptional(self):
        self._gotoTab("自选")
        return SelectedPage()

    def gotoMarketPrices(self):
        self._gotoTab("行情")
        import time
        time.sleep(5)
        self.handleTipsInMarket()
        return SelectedPage()

    def gotoHome(self):
        self._gotoTab("雪球")
        return self

    def gotoSearch(self):
        search_btn = (By.ID, "home_search")
        self.find(search_btn).click()
        return SearchPage()

    def _gotoTab(self, tab):
        self.findByText(tab).click()

    def handleTipsInMarket(self):
        if self.hasInfo("tips_wrapper"):
            self.swipeDown()

    def gotoProfile(self):
        self.find(MainPage._profile_button).click()
        return ProfilePage()
