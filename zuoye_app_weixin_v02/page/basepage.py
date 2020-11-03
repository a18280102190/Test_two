#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> basepage
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/1 17:41
@Desc   ：
=================================================='''
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

"""
基类，共用类,每个界面都会被使用到
"""
class BasePage():
    def __init__(self,driver: WebDriver = None):
        self.driver = driver




    def find(self,locator):

        return self.driver.find_element(*locator)
    #解元组

    def find_and_click(self,locator):
        logging.info('点击')
        self.find(locator).click()

    def find_and_sendkeys(self,locator,value):
        logging.info('输入')
        self.find(locator).send_keys(value)

    def find_by_scroll_and_click(self,text):
        logging.info('滚动查找')
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{text}").instance(0));')

        self.find(element).click()

    def get_toasttext(self):
        logging.info('获取Toast')
        text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(text)
        return text

    def get_results(self):
        logging.info('验证结果')
        text = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/c5m").text
        logging.info(text)
        return text