#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/6/2 17:54
@file        : loginpage.py
@description : 登录界面
"""
from selenium.webdriver.common.by import By

from AppiumDemo.pageobject.pages.basepage import BasePage


class LoginPage(BasePage):
    _close_locator = (By.ID, "iv_close")
    _other_locator = (By.ID, "tv_login_by_phone_or_others")
    _register_phone_number = (By.ID, "register_phone_number")
    _register_code = (By.ID, "register_code")
    _button_next = (By.ID, "button_next")
    _tv_login_with_account = (By.ID, "tv_login_with_account")
    _login_account = (By.ID, "login_account")
    _login_password = (By.ID, "login_password")
    _close2_locator = (By.ID, "iv_action_back")
    _error_msg = (By.ID, "md_content")
    _back_locator = (By.XPATH, "//*[contains(@resource-id, 'iv_close') or contains(@resource-id, 'iv_action_back')]")

    def loginByWx(self):
        return self

    def loginByMsg(self, phone, code):
        return self

    def loginByPassword(self, account, password):
        self.find(self._other_locator).click()
        self.find(self._tv_login_with_account).click()
        self.find(self._login_account).send_keys(account)
        self.find(self._login_password).send_keys(password)
        self.find(self._button_next).click()
        return self

    def back(self):
        self.find(self._back_locator).click()
        from AppiumDemo.pageobject.pages.profilepage import ProfilePage
        return ProfilePage()

    def getErrorMsg(self):
        msg = self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg
