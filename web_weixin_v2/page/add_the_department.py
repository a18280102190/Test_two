#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> add_the_department
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/12/2 17:39
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By

from web_weixin_v2.page.base_page import BasePage
from web_weixin_v2.page.contact_page import ContactPage
from time import sleep

class Add_the_department(BasePage):
    _dropdown = (By.CSS_SELECTOR,".js_create_dropdown .member_colLeft_top_addBtn")#点击添加+号
    _add_button = (By.CSS_SELECTOR, ".js_create_party")#点击添加部门
    _department_name = (By.CSS_SELECTOR , ".inputDlg_item:nth-child(1) .ww_inputText")#输入部门名称
    _Subordinate_departments = (By.CSS_SELECTOR, ".inputDlg_item:nth-child(3) .js_toggle_party_list") #选择所属部门
    _Click_departments = (By.CSS_SELECTOR, ".ww_dialog_body [id='1688851927989308_anchor']")#点击部门
    _confirm_button = (By.CSS_SELECTOR ,".ww_dialog_foot .ww_btn_Blue")#点击确定按钮
    _click_import = (By.CSS_SELECTOR ,".js_no_member .ww_btn_PartDropdown_left")#点击导入按钮
    _File_to_import = (By.CSS_SELECTOR , ".js_no_member .js_import_member:nth-child(1)")#点击文件导入
    _Upload_file = (By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask")#上传文件
    def click_add(self):
        self.click(self._dropdown)
        sleep(2)
        return self

    def click_add_button(self):
        self.click(self._add_button)
        return self

    def Enter_department_name(self,department_name):
        self.send_keys(self._department_name,department_name)
        return self

    def Subordinate_departments(self):
        self.click(self._Subordinate_departments)
        return self

    def Click_departments(self):
        self.click(self._Click_departments)
        return self

    def click_confirm_button(self):
        self.click(self._confirm_button)
        return self

    def click_import(self):
        self.click(self._click_import)
        return self

    def click_File_to_import(self):
        self.click(self._File_to_import)
        return self

    def click_Upload_file(self,file):
        self.send_keys(self._Upload_file,file)
        return ContactPage(self._driver)
