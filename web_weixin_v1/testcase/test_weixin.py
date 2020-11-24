#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_weixin
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/17 21:43
@Desc   ：
=================================================='''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage():
    _base_url = ""
    #_下划线是私有变量

    def __init__(self, driver: WebDriver = None):  # driver:WebDriver标识符
        if driver is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self._driver = webdriver.Chrome(options=option)
            # self._driver = webdriver.Chrome()
            #调用谷歌浏览器
            # self._driver.maximize_window()
            self._driver.implicitly_wait(5)

