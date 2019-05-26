#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/25 15:31
@file        : test_case0525.py
@description : 
"""
import pytest

from AppiumDemo.pageobject.pages.app import App


class TestCase0525(object):
    @classmethod
    def setup_class(cls):
        cls.main_page = App.app_main()

    def teardown_method(self):
        pass

    def test_price(self):
        price = self.main_page.gotoOptional().gotoHuS().getPriceName("格力电器")
        assert 53.90 == price
        self.main_page.gotoHome()

    def test_stock_index(self):
        index = self.main_page.gotoMarketPrices().gotoHuS().getStockIndex("深证成指")
        assert index >= 3000
        self.main_page.gotoHome()

    def test_is_selected_stock(self):
        searchPage = self.main_page.gotoSearch().searchFor("ali").gotoResFor()
        searchPage.addToSelected("00241")
        assert searchPage.isInSelected("00241")
        assert not searchPage.isInSelected("BABA")
        searchPage.cancelSearch()

    def test_is_follow_user(self):
        searchPage = self.main_page.gotoSearch().searchFor("zzw").gotoResByUser()
        searchPage.addFollow("zzw_")
        assert searchPage.isFollow("zzw_")
        assert not searchPage.isFollow("zzw")
        searchPage.cancelSearch()
