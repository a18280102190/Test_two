#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> wework_utils
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2021/8/29 14:19
@Desc   ：
=================================================='''
import requests

from Test_API.api_page.base_api import BaseApi


class WeWorkUtils(BaseApi):

    def get_token(self, corpsecret,  corpid = "ww75800c36b6f28af7"):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret,
            }
        }
        result = self.send_api(data)
        return result["access_token"]













