#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> clickeditbutton
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/2 14:53
@Desc   ：
=================================================='''
from appium.webdriver.common.mobileby import MobileBy

from zuoye_app_weixin_v02.page.basepage import BasePage


class ClickeDeitButton(BasePage):
    #点击编辑按钮
    deitbutton_element = (MobileBy.ID,"com.tencent.wework:id/hjz")
    def clickedeitbutton(self):
        self.find_and_click(self.deitbutton_element)

        from zuoye_app_weixin_v02.page.editmember import Editmember
        return Editmember(self.driver)



