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
        assert 52.31 == price
        self.main_page.gotoHome()

    def test_stock_index(self):
        index = self.main_page.gotoMarketPrices().gotoHuS().getStockIndex("深证成指")
        assert index >= 8000
        self.main_page.gotoHome()

    def test_is_selected_stock(self):
        tag = "00241"
        searchPage = self.main_page.gotoSearch().searchFor("ali").gotoResFor()
        if searchPage.isInSelected(tag):
            searchPage.removeFromSelected(tag)
        searchPage.addToSelected(tag)
        assert searchPage.isInSelected(tag)
        assert not searchPage.isInSelected("BABA")
        searchPage.cancelSearch()

    def test_is_follow_user(self):
        tag = "zzw_"
        searchPage = self.main_page.gotoSearch().searchFor("zzw").gotoResByUser()
        if searchPage.isFollowed(tag):
            searchPage.removeFollow(tag)
        searchPage.addFollow(tag)
        assert searchPage.isFollowed(tag)
        assert not searchPage.isFollowed("zzwen")
        searchPage.cancelSearch()
