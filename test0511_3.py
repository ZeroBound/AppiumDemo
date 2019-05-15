#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/5/14 22:05
@file        : test0511_3.py.py
@description :
完成雪球登录场景的测试
要求带有setup_class setup_method体系
微信 验证码 密码 错误的用户名 错误的密码 至少编写5条用例
"""
import allure
import pytest

# id
user_icon = "user_profile_icon"
login_btn = "tv_login"
wx_login_btn = "rl_login_by_wx"
other_login_btn = "tv_login_by_phone_or_others"
agreement = "service_agreement"

back_btn = "iv_action_back"
logo_icon = "iv_logo"
back_logo_contain = "sky_container"
register = "register_phone_number"
send_code = "register_code_text"
reg_code = "register_code"
login_next = "button_next"
acc_login = "tv_login_with_account"
login_more = "login_more"

# wei xin
jh = "android.widget.ScrollView"
acc_edit = "android.widget.EditText"  # 请填写微信号/QQ号/邮箱
pwd_edit = "android.widget.EditText"  #
wx_btn_cqc = "android.widget.Button"  # 登录
# 错误弹框

con = "android:id/content"
ok_btn = "com.tencent.mm:id/b00"  # android.widget.Button 确定
msg = "com.tencent.mm:id/d8x"  # android.widget.TextView 帐号或密码错误，请重新填写。

@pytest.fixture()
def login():
    print("login")
    yield
    print("logout")


@pytest.mark.parametrize()
@allure.story("手机号验证码登录")
def test_case01():
    print()


@pytest.mark.parametrize()
@allure.story("微信登录")
def test_case01():

    with allure.step(""):
        pass


if __name__ == "__main__":
    pytest.main([])
