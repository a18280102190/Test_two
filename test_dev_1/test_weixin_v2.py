#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_weixin_v2
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/20 14:38
@Desc   ：
=================================================='''
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeiXin2():


    def setup_class(self):
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown_class(self):
        pass

    def test_weixin(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']//a[2]/div").click()
        # sleep(2)
        pass

    # def test_cookies(self):
    #     # cookies = self.driver.get_cookies()
    #     # print(cookies)
    #     #获取cookies值
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
    #     cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851883153252'}, {'domain': 'work.weixin.qq.com', 'expiry': 1597938350.208574, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '17jpvi8'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'wqEDJfS7YlA9hHxCUcEHv_dvgKWZtAW6dyurWrmC7YoF4UGNMWTyEVvxaC9UiINc'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597906816'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629442814.208576, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '57712780513989'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629442815, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597839783,1597905439,1597906538,1597906816'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7571335'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'IdXbgm1itd4SWIDmjUtdimaSqesXPA1sddNZxn_HJaFyr6e_mjlQK3sbQMkJuUrufqj8z8lqRB3rWoStDhPjYswC5-9BbRzXevhhPRoET_LcoFiqRFYhBcC7Jw3vLkb4hX45hUEywart4aGzvUBDS2N26GpocD3lEo04nGj5ZUcjdH3UWk6asDJrklvvo-B1VyYYDTBI8qYndu0pEeB3Ez32m5d7Sz64tiVFSF4uDjfuJAM9_xJVNDrd4nHcFOS7CwAQ_PfLDsIU4d32KOxEBw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851883153252'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324988156941'}, {'domain': '.qq.com', 'expiry': 1597907088, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1660978827, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.86737757.1597906818'}, {'domain': '.qq.com', 'expiry': 1597993227, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1892286677.1597906818'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600499031.644273, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
    #     for cookie in cookies:
    #         if 'expiry' in cookie.keys():
    #             cookie.pop('expiry')
    #         self.driver.add_cookie(cookie)
    #         #放入cookie
    #
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
    #     #这个页面拿到cookie，才能打开
    #     sleep(2)
    #     self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']//a[2]/div").click()
    #     self.driver.find_element(By.ID,"js_upload_file_input").send_keys("C:/Users/asus/Desktop/自动化任务清单.xlsx")
    #     sleep(3)
    #     # 上传文件使用send_keys()
    #     assert "自动化任务清单.xlsx" == self.driver.find_element(By.ID,"upload_file_name").text
    #     sleep(3)

    def test_cookie1(self):

        # shelve 小型数据库 ，对象持久化保存方法
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851883153252'}, {'domain': 'work.weixin.qq.com', 'expiry': 1597938350.208574, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '17jpvi8'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'wqEDJfS7YlA9hHxCUcEHv_dvgKWZtAW6dyurWrmC7YoF4UGNMWTyEVvxaC9UiINc'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597906816'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629442814.208576, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '57712780513989'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629442815, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597839783,1597905439,1597906538,1597906816'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a7571335'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'IdXbgm1itd4SWIDmjUtdimaSqesXPA1sddNZxn_HJaFyr6e_mjlQK3sbQMkJuUrufqj8z8lqRB3rWoStDhPjYswC5-9BbRzXevhhPRoET_LcoFiqRFYhBcC7Jw3vLkb4hX45hUEywart4aGzvUBDS2N26GpocD3lEo04nGj5ZUcjdH3UWk6asDJrklvvo-B1VyYYDTBI8qYndu0pEeB3Ez32m5d7Sz64tiVFSF4uDjfuJAM9_xJVNDrd4nHcFOS7CwAQ_PfLDsIU4d32KOxEBw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851883153252'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324988156941'}, {'domain': '.qq.com', 'expiry': 1597907088, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1660978827, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.86737757.1597906818'}, {'domain': '.qq.com', 'expiry': 1597993227, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1892286677.1597906818'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600499031.644273, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]

        db = shelve.open("mydb/logincookies")
        #新建文件，并使用该文件，进行cookie保存
        # db['cookies'] = cookies
        # # 放在db cookie里
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
