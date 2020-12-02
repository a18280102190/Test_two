#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> contact_page
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/26 20:47
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By


from web_weixin_v2.page.base_page import BasePage


class ContactPage(BasePage):
    def go_to_add_meber(self):
        from web_weixin_v2.page.add_member_page import AddMember
        return AddMember(self._driver)



