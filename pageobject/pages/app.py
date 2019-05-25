#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/25 15:27
@file        : app.py
@description : App 级别
"""
from AppiumDemo.pageobject.drivers.androidclient import AndroidClient
from AppiumDemo.pageobject.pages.mainpage import MainPage


class App(object):
    @classmethod
    def app_main(cls):
        AndroidClient.init_driver()
        return MainPage()
