#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> Test_Api_01
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2021/8/16 21:49
@Desc   ：
=================================================='''
import requests

corpid = "ww75800c36b6f28af7"
corpsecret = "2ZzM5Wv8f92c7Ii9eNY-B7GeyE1a9sRJqbiYxlely_s"


def get_token():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    return result["access_token"]

def test_get():
    token = get_token()
    userid = "opopop"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
    print(requests.get(url).json())

def test_add():
    token = get_token()
    data = {
        "userid": "plplpl",
        "name": "老子",
        "mobile": "13800000011",
        "department": [1, 2],
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    print(requests.post(url, json=data).json())

def test_update():
    token = get_token()
    data1 = {
        "userid": "plplpl",
        "name": "老子",
        "mobile": "13800000012",
    }
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    print(requests.post(url, json=data1).json())



def test_delete():
    token = get_token()
    userid = "plplpl"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}"
    print(requests.get(url).json())
