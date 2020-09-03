#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> Base_Page
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/31 21:41
@Desc   ：
=================================================='''
from appium.webdriver.common.mobileby import MobileBy

from zuoye_app_weixin_v02.page.addresslistpage import AddressListPage
from zuoye_app_weixin_v02.page.basepage import BasePage
from zuoye_app_weixin_v02.page.selectname import SelectName
from time import sleep

class MainPage(BasePage):

    addressbook_elemenet = (MobileBy.XPATH, "//*[@text='通讯录']")
    back_button = (MobileBy.ID,"com.tencent.wework:id/hjo")
    #进入通讯录
    # addresslist_elemenet = MobileBy.XPATH, "//*[@text='添加成员']"
    def goto_addresslist(self):
        self.find_and_click(self.addressbook_elemenet)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # self.find_and_click(self.addresslist_elemenet)

        return AddressListPage(self.driver)


    def goto_back(self):
        pass

    def goto_addresslist_1(self):
        sleep(10)
        self.find_and_click(self.back_button)
        #返回通讯录
        self.find_and_click(self.addressbook_elemenet)
        #点击通讯录

        return SelectName(self.driver)