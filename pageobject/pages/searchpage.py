#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/25 15:27
@file        : searchpage.py
@description : 搜索页面
"""
import time
from selenium.webdriver.common.by import By

from AppiumDemo.pageobject.pages.basepage import BasePage


class SearchPage(BasePage):
    __item_child = "//*[contains(@resource-id, '{0}') and contains(@text, '{1}')]/ancestor::*[{2}]" \
                  "//*[contains(@resource-id, '{3}')]"

    def getStockBtn(self, name, follow_id):
        return self.__item_child.format("stockCode", name, 3, follow_id)

    def getUserBtn(self, name, follow_id):
        return self.__item_child.format("user_name", name, 2, follow_id)

    def cancelSearch(self):
        from AppiumDemo.pageobject.pages.mainpage import MainPage
        self.findById("action_close").click()
        return MainPage()

    def searchFor(self, key):
        _edit_text = (By.CLASS_NAME, "android.widget.EditText")
        self.find(_edit_text).send_keys(key)
        return self

    def gotoResFor(self, name="综合"):
        self.findByText(name).click()
        time.sleep(3)
        return self

    def addToSelected(self, name):
        follow_btn = (By.XPATH, self.getStockBtn(name, "/follow_btn"))
        self.find(follow_btn).click()
        self.hasTipMsg()
        return self

    def isInSelected(self, name):
        follow = (By.XPATH, self.getStockBtn(name, "/follow"))
        res = self.find(follow).get_attribute('resourceId')
        print(res)
        return 'followed_btn' in res

    def removeFromSelected(self, name):
        followed_btn = (By.XPATH, self.getStockBtn(name, "/followed_btn"))
        self.find(followed_btn).click()
        return self

    def gotoResByUser(self):
        return self.gotoResFor("用户")

    def addFollow(self, name):
        uesr_follow = (By.XPATH, self.getUserBtn(name, "/follow_btn"))
        self.find(uesr_follow).click()
        return self

    def removeFollow(self, name):
        uesr_followed = (By.XPATH, self.getUserBtn(name, "/followed_btn"))
        self.find(uesr_followed).click()
        return self

    def isFollowed(self, name):
        follow = (By.XPATH, self.getUserBtn(name, "/follow"))
        res = self.find(follow).get_attribute('resourceId')
        print(res)
        return 'followed_btn' in res

    def hasTipMsg(self):
        tip_close_id = "md_buttonDefaultNegative"
        for i in range(3):
            time.sleep(1)
            if self.hasInfo(tip_close_id):
                self.findById(tip_close_id).click()


