#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> base_api
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2021/8/29 11:11
@Desc   ：
=================================================='''
import json

import requests
class BaseApi:

    '''
    api 的抽象类
    '''
    def send_api(self, data: dict):
        '''
        发送Api
        '''
        print(json.dumps(data, indent=2))
        return requests.request(**data).json()