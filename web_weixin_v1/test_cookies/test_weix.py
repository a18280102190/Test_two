#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_weix
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/18 20:30
@Desc   ：
=================================================='''
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class TestDemo():
    # _下划线是私有变量
    def setup_method(self):
        # option = Options()
        # option.debugger_address = "localhost:9222"
        # self._driver = webdriver.Chrome(options=option)
        #浏览器复用
        self._driver = webdriver.Chrome()
        # 调用谷歌浏览器
        self._driver.maximize_window()
        self._driver.implicitly_wait(5)

    # def setup_method(self):
    #     self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    #
    # def teardown_method(self):
    #     self._driver.quit()

    # def test_clickadd(self):
    #     self._driver.find_element(By.ID,"menu_contacts").click()
    #
    # def test_comtact(self):
    #     #获取cookies
    #     cookies = self._driver.get_cookies()
    #     print(cookies)

    #     #打开网页
    #     self._driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    #     #使用cookies，代替浏览器复用
    #     #expiry': 1605733350,必须是整数
    #     cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851883153252'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'WqqsLkrQTer3qUsyq_RLAUTFbvRaDtMsJLnjJCX_eNF-K2y1ufm3za9ScseCYGZqSifaNIc7iFZXCipf_pzHo1UHLvA9N97PO21vCLiH8sk4K673NxiRCjgN9Qh6vbitADDJlQJDeobOzenJQBkyYSR4mp0C0nmxzQSlBtfMKVDbJKrMD0c8Go2EVpIr0rETEv2hed6mXCxSj0zlGbBpwPIJ9NCd6MO57j76luXMTyIQkBnoCQ8MNfbsigDWhqU3hj5WJ1dNJtXNqac_Li-Ypw'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851883153252'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324988156941'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'wqEDJfS7YlA9hHxCUcEHv4AY8bxL2Vrzmfa5zCwkCIQHg-1qeeCFOkHAFUI3Yvo0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3992810'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1605701822'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '01014375'}, {'domain': 'work.weixin.qq.com', 'expiry': 1605733350, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8lbodld'}, {'domain': '.qq.com', 'expiry': 1605788245, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1287968169.1605615584'}, {'domain': '.qq.com', 'expiry': 1668773845, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2007583986.1604892454'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636428449, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1608296081, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1637237821, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1605615573,1605618065,1605618213,1605701822'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5775190964'}, {'domain': '.qq.com', 'expiry': 1607954774, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1340839041'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '974a218cd850135e5e2e3df9426c1ae41f200c1b392fbf373b712deda8d47193'}, {'domain': '.qq.com', 'expiry': 1605704134, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '7462646784'}, {'domain': '.qq.com', 'expiry': 1880530160, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '1d10b1e5bf0ec8ff'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '96bZy3ccSn'}]
    #
    #     for cookie in cookies:
    #         if 'expiry' in cookie.keys():
    #             cookie.pop('expiry')
    #             #这个参数可删除，视为无用
    #         self._driver.add_cookie(cookie)
    #     sleep(3)
    #     # 打开网页
    #     self._driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    # # def test_clickadd(self):
    #     self._driver.find_element(By.ID,"menu_contacts").click()


    # def test_cookise1(self):
    #     cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851883153252'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '3pyfvYMDkBpDIwjpmWtLdabINhMX8o9oJ6IY7ayeJJ7J7LN4DYtpPeqDgbFYjT8gumDsidaB9QYoVyuVVg0TTDF0nnvWCF1NiFVINhyzxf7FRhufqsfvfDklIh3PX2LcL7E-TS29q05r5KALAb8nXlCQxgDscwupYuX2yk1qj255G9mGC3skxtL5AJLrZsYMiFNUMcS3uch_J98DcBo-O-O1P6irP5UstIT4v7UT0_z0zExBeRSRy9MGTLQPwBBlMxeyQcFC0moS7CclkUpJhA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851883153252'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324988156941'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'wqEDJfS7YlA9hHxCUcEHv-CNHuoiKEPKOMHArPL4waY1E2QZTXiGiA0gYOmUmPZH'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6811787'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1606221755'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '02553286'}, {'domain': '.qq.com', 'expiry': 1669293775, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2007583986.1604892454'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636428449, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1608815984, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1637757754, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1605618065,1605618213,1605701822,1606221755'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '5775190964'}, {'domain': '.qq.com', 'expiry': 1607954774, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1340839041'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '974a218cd850135e5e2e3df9426c1ae41f200c1b392fbf373b712deda8d47193'}, {'domain': '.qq.com', 'expiry': 1606308175, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1000584596.1606221757'}, {'domain': 'work.weixin.qq.com', 'expiry': 1606253288, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '3esn8i1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '7462646784'}, {'domain': '.qq.com', 'expiry': 1880530160, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '1d10b1e5bf0ec8ff'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '96bZy3ccSn'}]
    #
    #
    #     db = shelve.open("mydb/logincookies")
    #     db['cookise'] = cookies
    #             # 需要相同
    #     db.close()
    #     #以为数据库文件的形式进行保存cookies

    def test_cookies2(self):
        # shelve小型数据库，对象持久化保存方法
        #使用db 中的cookies
        db = shelve.open("mydb/logincookies")
        cookies = db['cookise']
                # 需要相同
        db.close()
        #访问需要访问的页面
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #使用保存的cookies
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
                # 这个参数可删除，视为无用
            self._driver.add_cookie(cookie)
        sleep(3)
        # 打开网页
        self._driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # def test_clickadd(self):
        # self._driver.find_element(By.ID, "menu_contacts").click()
        #点击通讯录

        # 导入联系人
        # 在控制台验证元素$('.index_service_cnt_itemWrap:nth-child(2)'),获取这个元素父节点的第二个子节点元素,CSS_SELECTOR方法
        self._driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(2)").click()
        #点击导入通讯录

        self._driver.find_element(By.CSS_SELECTOR,".ww_fileImporter_fileContainer_uploadInputMask").send_keys('C:/Users/asus/Desktop/通讯录批量导入.xlsx')
        #导入文件

        mydata = self._driver.find_element(By.CSS_SELECTOR,".ww_fileImporter_fileContainer_fileNames").text
        assert '通讯录批量导入.xlsx' == mydata
        sleep(3)

