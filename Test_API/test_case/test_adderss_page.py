#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_adderss_page
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2021/8/29 11:23
@Desc   ：
=================================================='''
from Test_API.api_page.address_page import AdderssPage


class TestAddressPage:
    def setup_class(self):
        self.address_page = AdderssPage()

    def test_get(self):
        membet_message = self.address_page.get_member_info()
        assert membet_message['errcode'] == 0
        print(membet_message)

    def test_add(self):
        membet_message = self.address_page.add_member()
        assert membet_message['errcode'] == 0

    def test_update(self):
        membet_message = self.address_page.update_member()
        assert membet_message['errcode'] == 0

    def test_delete(self):
        membet_message = self.address_page.delete_member()
        assert membet_message['errcode'] == 0



