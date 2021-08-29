#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> Test_Api_01_1
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2021/8/29 10:21
@Desc   ：
=================================================='''

import requests

corpid = "ww75800c36b6f28af7"
corpsecret = "2ZzM5Wv8f92c7Ii9eNY-B7GeyE1a9sRJqbiYxlely_s"


def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result["access_token"]

def test_add_01():
    toekn = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={toekn}"
    data = {
        "name": "成都测试中心",
        "name_en": "zZZ",
        "parentid": 1,
    }
    print(requests.post(url, json=data).json())

def test_update1():
    toekn = get_token()
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={toekn}"
    data = {
            "id": 3,
            "name": "成都测试中心3",
        }

    print(requests.post(url, json=data).json())

def test_get1():
    token = get_token()
    id = "航航企业1"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={token}&id={id}"
    print(requests.get(url).json())


def test_delete():
    token = get_token()
    id1 = 4
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={token}&id={id1}"
    print(requests.get(url).json())