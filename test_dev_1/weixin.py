#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> weixin
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/18 21:23
@Desc   ：
=================================================='''
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeixin():
    def setup_class(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # self.driver.maximize_window()
        # 浏览器复用不能使用窗口最大化
        self.driver.implicitly_wait(5)

    # def setup_class(self):
    #     # 创建一个选项options
    #     option = webdriver.ChromeOptions()
    #     # 创建一个远程ip端口9222
    #     option.debugger_address = "localhost:9222"
    #     # 把选项应用到Chrome浏览器中
    #     self.driver = webdriver.Chrome(options=option)

    def teardown_class(self):
        # self.driver.quit()
        pass


    def test_weixin(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']//a[2]/div").click()
        sleep(2)


    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # #捕捉cookies
        # print(cookies)
        # sleep(3)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        #打开页面，先访问需要访问的页面
        cookies = [{'domain': '.work.weixin.qq.com',
                    'httpOnly': True,
                    'name': 'wwrtx.vst',
                    'path': '/',
                    'secure': False,
                    'value': 'SAnkfisnIbiG4Ws-6AbU52XSeXVXcNsrfCIowDYyHJoAujYFTElq0tt9hQdiA88Hbjt5pX1BEeIEZrwRLJfutR2GNATdl1oBCccmDKL6mv24KcnL-kqcuGFdbP9ub_kwypwVGdLSTT2laMD2Yk4viHtMVPbJIKmZQojVuOaCeWg53xczDwZmhZXfDdV5MrAp5CPglOOC43l6nvYJYpVg0Y9mWrTENKcQilRXoZzjxhwe3gTDEhVIwcTRqdyQlDMbW1ZIg4633TXmVXiYu8DNUw'},
                   {'domain': '.work.weixin.qq.com',
                    'expiry': 1629381684.678888,
                    'httpOnly': False,
                    'name': 'wwrtx.c_gdpr',
                    'path': '/',
                    'secure': False,
                    'value': '0'},
                   {'domain': '.work.weixin.qq.com',
                    'httpOnly': True,
                    'name': 'wwrtx.ref',
                    'path': '/',
                    'secure': False,
                    'value': 'direct'},
                   {'domain': '.work.weixin.qq.com',
                    'httpOnly': True,
                    'name': 'wwrtx.refid',
                    'path': '/',
                    'secure': False,
                    'value': '085344'},
                   {'domain': '.work.weixin.qq.com',
                    'httpOnly': False,
                    'name': 'wxpay.vid',
                    'path': '/',
                    'secure': False,
                    'value': '1688851883153252'},
                   {'domain': 'work.weixin.qq.com',
                    'expiry': 1597877220.678891,
                    'httpOnly': True,
                    'name': 'ww_rtkey',
                    'path': '/',
                    'secure': False,
                    'value': '4blqpgl'},
                   {'domain': '.work.weixin.qq.com',
                    'httpOnly': True,
                    'name': 'wwrtx.ltype',
                    'path': '/',
                    'secure': False,
                    'value': '1'},
                   {'domain': '.work.weixin.qq.com',
                    'httpOnly': True,
                    'name': 'wwrtx.sid',
                    'path': '/',
                    'secure': False,
                    'value': 'wqEDJfS7YlA9hHxCUcEHv8vftOpiewJveCHSWuITY1VR3l7G4MTQHUnGIjQjGcOK'},
                   {'domain': '.work.weixin.qq.com',
                    'httpOnly': False,
                    'name': 'wwrtx.vid',
                    'path': '/',
                    'secure': False,
                    'value': '1688851883153252'},
                   {'domain': '.work.weixin.qq.com',
                    'httpOnly': False,
                    'name': 'wwrtx.d2st',
                    'path': '/',
                    'secure': False,
                    'value': 'a2612780'},
                   {'domain': '.work.weixin.qq.com',
                    'httpOnly': False,
                    'name': 'wxpay.corpid',
                    'path': '/',
                    'secure': False,
                    'value': '1970324988156941'},
                   {'domain': '.qq.com',
                    'expiry': 1660921949,
                    'httpOnly': False,
                    'name': '_ga',
                    'path': '/',
                    'secure': False,
                    'value': 'GA1.2.1096302254.1597845686'},
                   {'domain': '.qq.com',
                    'expiry': 1597936349,
                    'httpOnly': False,
                    'name': '_gid',
                    'path': '/',
                    'secure': False,
                    'value': 'GA1.2.702402411.1597845686'},
                   {'domain': '.work.weixin.qq.com',
                    'expiry': 1600441973.017351,
                    'httpOnly': False,
                    'name': 'wwrtx.i18n_lan',
                    'path': '/',
                    'secure': False,
                    'value': 'zh-cn'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
            #放入cookie

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        #这个页面拿到cookie，才能打开
        sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']//a[2]/div").click()
        self.driver.find_element(By.ID,"js_upload_file_input").send_keys("C:/Users/asus/Desktop/自动化任务清单.xlsx")
        sleep(3)
        # 上传文件使用send_keys()
        assert "自动化任务清单.xlsx" == self.driver.find_element(By.ID,"upload_file_name").text
        sleep(3)


    def test_cookie1(self):
        #shelve 小型数据库 ，对象持久化保存方法
        pass

        # cookies = [{'domain': '.work.weixin.qq.com',
        #         'httpOnly': True,
        #         'name': 'wwrtx.vst',
        #         'path': '/',
        #         'secure': False,
        #         'value': 'SAnkfisnIbiG4Ws-6AbU52XSeXVXcNsrfCIowDYyHJoAujYFTElq0tt9hQdiA88Hbjt5pX1BEeIEZrwRLJfutR2GNATdl1oBCccmDKL6mv24KcnL-kqcuGFdbP9ub_kwypwVGdLSTT2laMD2Yk4viHtMVPbJIKmZQojVuOaCeWg53xczDwZmhZXfDdV5MrAp5CPglOOC43l6nvYJYpVg0Y9mWrTENKcQilRXoZzjxhwe3gTDEhVIwcTRqdyQlDMbW1ZIg4633TXmVXiYu8DNUw'},
        #        {'domain': '.work.weixin.qq.com',
        #         'expiry': 1629381684.678888,
        #         'httpOnly': False,
        #         'name': 'wwrtx.c_gdpr',
        #         'path': '/',
        #         'secure': False,
        #         'value': '0'},
        #        {'domain': '.work.weixin.qq.com',
        #         'httpOnly': True,
        #         'name': 'wwrtx.ref',
        #         'path': '/',
        #         'secure': False,
        #         'value': 'direct'},
        #        {'domain': '.work.weixin.qq.com',
        #         'httpOnly': True,
        #         'name': 'wwrtx.refid',
        #         'path': '/',
        #         'secure': False,
        #         'value': '085344'},
        #        {'domain': '.work.weixin.qq.com',
        #         'httpOnly': False,
        #         'name': 'wxpay.vid',
        #         'path': '/',
        #         'secure': False,
        #         'value': '1688851883153252'},
        #        {'domain': 'work.weixin.qq.com',
        #         'expiry': 1597877220.678891,
        #         'httpOnly': True,
        #         'name': 'ww_rtkey',
        #         'path': '/',
        #         'secure': False,
        #         'value': '4blqpgl'},
        #        {'domain': '.work.weixin.qq.com',
        #         'httpOnly': True,
        #         'name': 'wwrtx.ltype',
        #         'path': '/',
        #         'secure': False,
        #         'value': '1'},
        #        {'domain': '.work.weixin.qq.com',
        #         'httpOnly': True,
        #         'name': 'wwrtx.sid',
        #         'path': '/',
        #         'secure': False,
        #         'value': 'wqEDJfS7YlA9hHxCUcEHv8vftOpiewJveCHSWuITY1VR3l7G4MTQHUnGIjQjGcOK'},
        #        {'domain': '.work.weixin.qq.com',
        #         'httpOnly': False,
        #         'name': 'wwrtx.vid',
        #         'path': '/',
        #         'secure': False,
        #         'value': '1688851883153252'},
        #        {'domain': '.work.weixin.qq.com',
        #         'httpOnly': False,
        #         'name': 'wwrtx.d2st',
        #         'path': '/',
        #         'secure': False,
        #         'value': 'a2612780'},
        #        {'domain': '.work.weixin.qq.com',
        #         'httpOnly': False,
        #         'name': 'wxpay.corpid',
        #         'path': '/',
        #         'secure': False,
        #         'value': '1970324988156941'},
        #        {'domain': '.qq.com',
        #         'expiry': 1660921949,
        #         'httpOnly': False,
        #         'name': '_ga',
        #         'path': '/',
        #         'secure': False,
        #         'value': 'GA1.2.1096302254.1597845686'},
        #        {'domain': '.qq.com',
        #         'expiry': 1597936349,
        #         'httpOnly': False,
        #         'name': '_gid',
        #         'path': '/',
        #         'secure': False,
        #         'value': 'GA1.2.702402411.1597845686'},
        #        {'domain': '.work.weixin.qq.com',
        #         'expiry': 1600441973.017351,
        #         'httpOnly': False,
        #         'name': 'wwrtx.i18n_lan',
        #         'path': '/',
        #         'secure': False,
        #         'value': 'zh-cn'}]
        #先把cookies放在，
        db = shelve.open("mydb/logincookies")
        #新建文件，并使用该文件，进行cookie保存
        # db['cookies'] = cookies
        #放在db cookie里
        # cookies = db['cookies']
        # db.close()
        # 自动保存cookie
        cookies = db['cookies']
        #通过db cookie ，获取刚刚存入cookie
        db.close()

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']//a[2]/div").click()
        self.driver.find_element(By.ID,"js_upload_file_input").send_keys("C:/Users/asus/Desktop/自动化任务清单.xlsx")
        sleep(3)
        # 上传文件使用send_keys()
        assert "自动化任务清单.xlsx" == self.driver.find_element(By.ID,"upload_file_name").text