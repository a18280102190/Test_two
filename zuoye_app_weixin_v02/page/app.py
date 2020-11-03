#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> app
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/31 21:42
@Desc   ：
=================================================='''
from appium import webdriver

from zuoye_app_weixin_v02.page.basepage import BasePage
from zuoye_app_weixin_v02.page.main_page import MainPage

"""
App 类： 
app常用的方法：比如：启动应用，关闭应用，重启应用，进入首页
"""

class App(BasePage):

    def start(self):
        #启动
        """
        如果driver已经被实例化，就复用已有的driver
        如果driver =None ，就要重新创建一个driver
        """
        if self.driver == None:
            desire_cap2s = {}
            desire_cap2s['platformName'] = 'android'
                # 平台的名字
            desire_cap2s['deviceName'] = '127.0.0.1:7555'
                # 设备的名字
            desire_cap2s['appPackage'] = 'com.tencent.wework'
            desire_cap2s['appActivity'] = '.launch.WwMainActivity'
            desire_cap2s['noReset'] = 'true'
            desire_cap2s['dontStopAppOnReset'] = 'true'
            desire_cap2s['unicodeKeyBoard'] = 'true'
            desire_cap2s['resetKeyBoard'] = 'true'

            self.driver = webdriver.Remote("http://192.168.75.1:4723/wd/hub", desire_cap2s)
            self.driver.implicitly_wait(15)
        else:
            self.driver.launch_app()
            #启动任何一个包和appActivity
            # self.driver.start_activity()
            #需要包名和appActivity

        return self

    def restart(self):
        #重启
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        #关闭
        self.driver.quit()

    def goto_main(self) ->MainPage:
        #进入首页

        return MainPage(self.driver)



