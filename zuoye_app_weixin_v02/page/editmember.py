#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> editmember
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/2 14:59
@Desc   ：
=================================================='''
from appium.webdriver.common.mobileby import MobileBy

from zuoye_app_weixin_v02.page.basepage import BasePage


class Editmember(BasePage):
    #点击编辑成员
    editmember_element = (MobileBy.ID,"com.tencent.wework:id/b53")

    def editmember(self):
        self.find_and_click(self.editmember_element)

        from zuoye_app_weixin_v02.page.deletename import DeleteName
        return DeleteName(self.driver)
