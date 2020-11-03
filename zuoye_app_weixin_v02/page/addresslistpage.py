#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> addresslistpage
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/1 15:36
@Desc   ：
=================================================='''
from appium.webdriver.common.mobileby import MobileBy

from zuoye_app_weixin_v02.page.basepage import BasePage
from zuoye_app_weixin_v02.page.memberlnvitepage import MemberInvitePage


class AddressListPage(BasePage):

    addmember_text = "添加成员"
    def add_member(self):
        '''
        添加成员

        '''
        #MemberInvitePage
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()
        self.find_by_scroll_and_click(self.addmember_text)
        #滚动查找
        #点击添加成员按钮
        return MemberInvitePage(self.driver)
