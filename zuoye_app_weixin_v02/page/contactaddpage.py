#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> contactaddpage
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/1 15:42
@Desc   ：
=================================================='''
from appium.webdriver.common.mobileby import MobileBy

from zuoye_app_weixin_v02.page.basepage import BasePage
from time import sleep

class ContactAddPage(BasePage):
    name_element = (MobileBy.XPATH,"//*[@text='必填']")
    gender_element = (MobileBy.XPATH,"//*[@text='男']")
    male_element = (MobileBy.XPATH,"//*[@text='男']")
    female_element = (MobileBy.XPATH,"//*[@text='女']")
    phonenum_element = (MobileBy.ID,"com.tencent.wework:id/f9s")
    seve_element = (MobileBy.ID,"com.tencent.wework:id/hk6")




    def edit_name(self,name):
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='必填']").send_keys(name)
        self.find_and_sendkeys(self.name_element,name)
        #填写姓名
        return self

    def edit_gender(self,gender):
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        # #点击男，将会弹出选择对话框
        # if gender == '男':
        #     self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        self.find_and_click(self.gender_element)
        if gender == '男':
            sleep(10)
            self.find_and_click(self.male_element)
        else:
            self.find_and_click(self.female_element)
        return self

    def edit_phonenum(self,phonenum):
        # self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/f9s").send_keys(phonenum)
        sleep(10)
        self.find_and_sendkeys(self.phonenum_element,phonenum)
        #输入电话号码
        return  self

    def click_save(self):

        from zuoye_app_weixin_v02.page.memberlnvitepage import MemberInvitePage
        # self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hk6").click()
        self.find_and_click(self.seve_element)
        #点击保存
        return MemberInvitePage(self.driver)
