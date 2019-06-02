#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author      : zzw
@time        : 2019/6/1 9:48
@file        : testyaml.py
@description : yaml 数据测试
"""
import yaml

file_name = r"..\data\loginpage.yml"


class TestYaml(object):
    def test_yaml(self):
        with open(file_name, 'r') as file:
            d = yaml.load(file, Loader=yaml.FullLoader)
            print(type(d), d)
            po = d["loginByPassword"]
            for i in po:
                print(type(i), i)


if __name__ == "__main__":
    TestYaml().test_yaml()
