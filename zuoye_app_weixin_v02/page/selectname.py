#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> ClickBack
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/2 13:53
@Desc   ：
=================================================='''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from zuoye_app_weixin_v02.page.basepage import BasePage


class SelectName(BasePage):
    #选择成员
    click_back_element = (MobileBy.XPATH,"//*[@text='zh1']")
    def select_name(self):

        sleep(10)
        self.find_and_click(self.click_back_element)

        from zuoye_app_weixin_v02.page.clickeditbutton import ClickeDeitButton
        return ClickeDeitButton(self.driver)