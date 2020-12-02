#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> base_page
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/26 21:14
@Desc   ：
=================================================='''
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

#组合定位(".qui_dialog_body.ww_dialog_body [id='1688851927989308_anchor']")
class BasePage:
    _url = ""
    # Windows：chrome --remote-debugging-port=9222浏览器复用
    def __init__(self, driver_base = None):
        if driver_base is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)
            #浏览器复用
            # self._driver = webdriver.Chrome()
            # 调用谷歌浏览器
            # self._driver.maximize_window()

        else:
            self._driver: WebDriver = driver_base
        if self._url != "":
            self._driver.get(self._url)
        self._driver.implicitly_wait(5)

    def find(self,locator):
        logging.info('元素定位')
        return self._driver.find_element(*locator)

    def finds(self,*locator):
        logging.info('元素查找')
        return self._driver.find_elements(*locator)

    def click(self,locator):
        logging.info('点击')
        self.find(locator).click()

    def send_keys(self,locator,value):
        logging.info('输入')
        self.find(locator).send_keys(value)
    _ww_inputWithTips_WithErr = (By.CSS_SELECTOR, ".ww_inputWithTips_WithErr .ww_inputWithTips_tips")
    def get_phone_error_messrge(self):
        text = self.find(self._ww_inputWithTips_WithErr).text
        logging.info('请输入正确的手机号')
        return text
        #层级定位（父级到子级）

    _member_colRight_memberTable_td = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    def get_member_list(self):
        name_list = self.finds(self._member_colRight_memberTable_td)
        #查找元素并打印出来
        # print(name_list)
        #列表推导式
        list1 = []
        for name in name_list:
            list1.append(name.text)
        print(list1)
        return list1

    _ww_tip_success = (By.CSS_SELECTOR, ".ww_tip.success")
    def get_member_list1(self):
        text = self.find(self._ww_tip_success).text
        logging.info('保存成功')
        return text
    _ww_fileImporter_fileContainer_fileNames = (By.CSS_SELECTOR,".ww_fileImporter_fileContainer_fileNames")
    def get_meber_list2(self):
        text = self.find(self._ww_fileImporter_fileContainer_fileNames).text
        logging.info('通讯录批量导入.xlsx')
        return text



    def base_quit(self):
        return self._driver.quit()