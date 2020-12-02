#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> add_member_page
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/26 20:47
@Desc   ：
=================================================='''
from selenium import webdriver
from selenium.webdriver.common.by import By

from web_weixin_v2.page.base_page import BasePage
from web_weixin_v2.page.contact_page import ContactPage


class AddMember(BasePage):
    _username = (By.ID, 'username')
    _memberAdd_acctid = (By.ID, 'memberAdd_acctid')
    _memberAdd_phone = (By.ID, 'memberAdd_phone')
    _js_btn_save = (By.CSS_SELECTOR, '.js_btn_save')
    def add_member(self, name):
        # driver = webdriver.Chrome()
        # self.find(*self._username).send_keys('zh5')
        self.send_keys(self._username,name)
        return self
        # self._driver.find_element(By.ID, 'username').send_keys('zh5')
        # 输入姓名
    def input_acctid(self,acctid):
        # self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys('123123')
        self.send_keys(self._memberAdd_acctid,acctid)
        return self
        # 输入账号
    def input_phone(self,phone):
        # self._driver.find_element(By.ID, 'memberAdd_phone').send_keys('18211111111')
        # self._driver.find_element(By.ID, 'memberAdd_phone').send_keys(phone)
        self.send_keys(self._memberAdd_phone,phone)
        return self
        # 输入手机号
        # self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
    def click_button(self):
        self.click(self._js_btn_save)
        # 点击保存
        return ContactPage(self._driver)



