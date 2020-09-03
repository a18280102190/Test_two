#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> deletename
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/2 15:15
@Desc   ：
=================================================='''
from appium.webdriver.common.mobileby import MobileBy

from zuoye_app_weixin_v02.page.basepage import BasePage
from time import sleep

class DeleteName(BasePage):

    sleep(10)
    deletename_element = '删除成员'
    confirm_element = (MobileBy.ID,"com.tencent.wework:id/bfe")
    search_element = (MobileBy.ID,"com.tencent.wework:id/hk9")
    search_id_element = (MobileBy.ID,"com.tencent.wework:id/g75")

    def deletename(self):
        self.find_by_scroll_and_click(self.deletename_element)
        # 点击删除按钮
        from zuoye_app_weixin_v02.page.main_page import MainPage
        return self

    def confirm(self):
        self.find_and_click(self.confirm_element)
        # 点击确认按钮
        return self

    def search(self):
        sleep(10)
        # 点击搜索按钮
        self.find_and_click(self.search_element)
        return self

    def search_name_id(self,value):
        sleep(10)
        self.find_and_sendkeys(self.search_id_element,value)
        return self

