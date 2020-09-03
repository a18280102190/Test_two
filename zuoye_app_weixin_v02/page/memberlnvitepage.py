#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> memberlnvitepage
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/1 15:40
@Desc   ：
=================================================='''
from appium.webdriver.common.mobileby import MobileBy

from zuoye_app_weixin_v02.page.basepage import BasePage
from time import sleep

class MemberInvitePage(BasePage):
    addmember_menul_element = (MobileBy.XPATH,"//*[@text='手动输入添加']")


    def addmember_menual(self):

        from zuoye_app_weixin_v02.page.contactaddpage import ContactAddPage
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        sleep(10)
        self.find_and_click(self.addmember_menul_element)
        #点击手动输入按钮
        return ContactAddPage(self.driver)


    def get_toast(self):
        # toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        # assert '添加成功' == toasttext
        toasttext = self.get_toasttext()
        return toasttext

