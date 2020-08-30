#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_app_weixin_v1
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/27 22:29
@Desc   ：
=================================================='''
from appium import webdriver
from time import sleep
#创建desire_cap对象，字典类型的
from selenium.webdriver.common.by import By

desire_cap = {
  "platformName": "android",
  #平台的名字
  "deviceName": "127.0.0.1:7555",
  #设备的名字
  "appPackage": "com.xueqiu.android",
  "appActivity": ".view.WelcomeActivityAlias",
  "noReset": True,
  "dontStopAppOnReset" : True

}
def test_xueqiu():
  #"dontStopAppOnReset" : True,挺高app的速度
  driver = webdriver.Remote("http://192.168.220.1:4723/wd/hub",desire_cap)
  driver.implicitly_wait(10)

  driver.find_element(By.ID,"com.xueqiu.android:id/tv_search").click()
  #点击搜索框
  driver.find_element(By.ID,"com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
  #输入阿里巴巴
  #返回上一个页面
# driver.quit()