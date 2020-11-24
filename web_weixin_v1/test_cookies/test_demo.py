#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_demo
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/18 20:24
@Desc   ：
=================================================='''
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.opera.options import Options


class TestDemo():

    #_下划线是私有变量
    def setup_method(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        self._driver = webdriver.Chrome(options=option)
        # self._driver = webdriver.Chrome()
        #调用谷歌浏览器
        # self._driver.maximize_window()
        self._driver.implicitly_wait(5)
    def teardown_method(self):
        self._driver.quit()
    def clickadd(self):
        self.find(By.CSS_SELECTOR,".member_colLeft_top_addBtn").click()
