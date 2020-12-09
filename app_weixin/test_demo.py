#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_demo
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/12/7 21:57
@Desc   ：
=================================================='''
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
def get_contact():
    with open("./datas/contacts.yaml",encoding='utf-8') as f:
        #读取这个文件
        datas = yaml.safe_load(f)
        add_datas = datas['add']
        add_delete = datas['delete']
    return [add_datas,add_delete]

class TestDemo:
    def setup(self):
        #启动
        """
        如果_driver已经被实例化，就复用已有的_driver
        如果_driver =None ，就要重新创建一个_driver
        """

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

        self._driver = webdriver.Remote("http://192.168.75.1:4723/wd/hub", desire_cap2s)
        self._driver.implicitly_wait(15)


    def teardown(self):
        self._driver.quit()
    @pytest.mark.parametrize('phone_number,gender,name',get_contact()[0])
    def test_sendmess(self,phone_number,gender,name):
        self._driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        #点击通讯录
        self._driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        #滚动查找
        self._driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        #点击手动输入按钮

        self._driver.find_element(MobileBy.XPATH,"//*[@text='必填']").send_keys(name)
        #填写姓名
        self._driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        #点击男，将会弹出选择对话框
        if gender == '男':
            self._driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self._driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/f9s").send_keys(phone_number)
        #输入电话号码
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/hk6").click()
        #点击保存
        sleep(2)
        # toast 弹框,打印当前页面的布局结构 ，xml 结构
        # print(self._driver.page_source)
        toasttext = self._driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == toasttext
        #进行断言操作，验证是否添加成功
        
    @pytest.mark.parametrize('name',get_contact()[1])
    def test_xueqiu_delete(self,name):
        # name = 'zh1'
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/hjo").click()
        #点击返回
        self._driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击通讯录按钮
        self._driver.find_element(MobileBy.XPATH,"//*[@text='zh1']").click()
        #选择成员ID
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/hjz").click()
        #点击编辑按钮
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/b53").click()
        #点击编辑成员按钮
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/e_1").click()
        #点击删除成员按钮
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/bfe").click()
        #点击确认按钮
        sleep(2)
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/hk9").click()
        #点击搜索按钮
        self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/g75").send_keys(name)
        #输入需要搜索的员工ID
        results = self._driver.find_element(MobileBy.ID,"com.tencent.wework:id/c5m").text
        print(results)
        assert results == '无搜索结果'