#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> page
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/26 20:46
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By


from web_weixin_v2.page.add_member_page import AddMember
from web_weixin_v2.page.add_the_department import Add_the_department
from web_weixin_v2.page.base_page import BasePage
from web_weixin_v2.page.contact_page import ContactPage
from selenium import webdriver

class MainPage(BasePage):
    _memberAdd_phone = ""
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"
    # _addmember = (By.CSS_SELECTOR, "[node-type='addmember']")
    _addmember = (By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)")
    _book = (By.ID, 'menu_contacts')
    def go_to_contact(self):

        return ContactPage(self._driver)

    def go_to_add_member(self):
        # dirver = webdriver.Chrome()
        self.click(self._addmember)
        #点击添加成员
        return AddMember(self._driver)

    def go_to_address_book(self):
        self.click(self._book)
        #点击通讯录
        return Add_the_department(self._driver)