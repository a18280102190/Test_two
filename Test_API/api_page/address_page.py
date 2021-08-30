#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> address_page
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2021/8/29 11:09
@Desc   ：
=================================================='''
import requests
import random

from Test_API.api_page.base_api import BaseApi
from Test_API.api_page.wework_utils import WeWorkUtils


class AdderssPage(BaseApi):
    '''
    通讯录管理， 包括正删改查

    '''
    def __init__(self):
        _corpsecret = "2ZzM5Wv8f92c7Ii9eNY-B7GeyE1a9sRJqbiYxlely_s"
        utils = WeWorkUtils()
        self.token = utils.get_token(_corpsecret)


    def add_member(self):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/create",
            "params": {"access_token":self.token},
            "json":{
                "userid": "plplprr2r",
                "name": "干饭5",
                "mobile": "13800000077",
                "department": [1]}}
        return self.send_api(data)

    def delete_member(self):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params":{"access_token":self.token,"userid":"plplprr2r"}

        }
        return self.send_api(data)

    def update_member(self):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}",
            "json":{
                "userid": "plplprr2r",
                "name": "干饭",
                "mobile": "13800000030",
            }
        }
        return self.send_api(data)

    def get_member_info(self):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params": {"access_token": self.token, "userid" : "opopop"}
        }
        return self.send_api(data)



