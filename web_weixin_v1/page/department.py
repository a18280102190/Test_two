#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> department
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/23 13:46
@Desc   ：
=================================================='''
from selenium.webdriver.common.by import By
from time import sleep

from web_weixin_v1.page.base_page import BasePage


class Department(BasePage):
    def department(self):
        deptName = 'QA部门'
        self.find(By.XPATH,"//*[@id='__dialog__MNDialog__']//form/div[1]/input").send_keys(deptName)

        self.find(By.CSS_SELECTOR,".js_parent_party_name").click()

        self.find(By.CSS_SELECTOR, ".qui_dialog_body.ww_dialog_body [id='1688851927989308_anchor']").click()
        #组合定位
        self.find(By.XPATH,"//*[@id='__dialog__MNDialog__']/div/div[3]/a[1]").click()

    # def get_departments_list(self):
        departments_name_list = self.finds(By.XPATH, "//ul[@class='jstree-children']//li[last()]")
        sleep(3)
        #//代表子孙元素,先定位到页面符合我条件的ul元素,然后找它的所有子孙li元素,li找倒数第一个
        return [item.text for item in departments_name_list]


