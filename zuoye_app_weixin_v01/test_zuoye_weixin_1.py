#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_zuoye_weixin
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/30 16:41
@Desc   ：
=================================================='''
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def get_contact():
    with open("./datas/contacts.yaml",encoding='utf-8') as f:
        #读取这个文件
        datas = yaml.safe_load(f)
    return datas



class TestDW():
    def setup(self):
        desire_cap1s = {}
        desire_cap1s['platformName'] = 'android'
            # 平台的名字
        desire_cap1s['deviceName'] = '127.0.0.1:7555'
            # 设备的名字
        desire_cap1s['appPackage'] = 'com.tencent.wework'
        desire_cap1s['appActivity'] = '.launch.WwMainActivity'
        desire_cap1s['noReset'] = 'true'
        desire_cap1s['dontStopAppOnReset'] = 'true'
        desire_cap1s['unicodeKeyBoard'] = 'true'
        desire_cap1s['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote("http://192.168.220.1:4723/wd/hub", desire_cap1s)
        self.driver.implicitly_wait(15)

    def teardown(self):
        # self.driver.quit()
        pass

    @pytest.mark.parametrize('phone_number,gender,name',get_contact())
    def test_xueqiu_add(self,phone_number,gender,name):
        # phone_number = 12345679806
        # gender = '男'
        # name = 'zh1'
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        #点击通讯录按钮
        # self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()
        #滚动查找
        #点击添加成员按钮
        sleep(10)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        # Element = WebDriverWait(self.driver,10,0.5).until(\
        #     expected_conditions.visibility_of_element_located((MobileBy.XPATH,"//*[@text='手动输入添加']")))
        #显示等待
        # print(Element)
        #点击手动输入按钮

        self.driver.find_element(MobileBy.XPATH,"//*[@text='必填']").send_keys(name)
        #填写姓名
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        #点击男，将会弹出选择对话框
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/f9s").send_keys(phone_number)
        #输入电话号码
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hk6").click()
        #点击保存
        sleep(2)
        # toast 弹框,打印当前页面的布局结构 ，xml 结构
        # print(self.driver.page_source)
        toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == toasttext
        #进行断言操作，验证是否添加成功

    @pytest.mark.parametrize('name',get_contact())
    def test_xueqiu_delete(self,name):
        # name = 'zh1'
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 点击通讯录按钮
        self.driver.find_element(MobileBy.XPATH,"//*[@text='zh1']").click()
        #选择成员ID
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hjz").click()
        #点击编辑按钮
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b53").click()
        #点击编辑成员按钮
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/e_1").click()
        #点击删除成员按钮
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/bfe").click()
        #点击确认按钮
        sleep(2)
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/hk9").click()
        #点击搜索按钮
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/g75").send_keys(name)
        #输入需要搜索的员工ID
        results = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/c5m").text
        print(results)
        assert results == '无搜索结果'