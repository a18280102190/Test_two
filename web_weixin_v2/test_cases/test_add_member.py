#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_add_member
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/26 20:55
@Desc   ：
=================================================='''
import pytest
import yaml

from web_weixin_v2.page.mian_page import MainPage

def get_contact():
    with open("../value_data/data.yaml",encoding='utf-8') as f:
        value_data = yaml.safe_load(f)
        add_members = value_data['addname1']
        add_members1 = value_data['addname2']
        add_members2 = value_data['addname3']
        del_members = value_data['delname']
    return [add_members,add_members1,add_members2,del_members]



class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    @pytest.mark.parametrize('name,acctid ,phone',get_contact()[1])
    def test_add_member(self,name,acctid ,phone):
        #1.跳转到添加成员 2.添加成员
        # result = self.main.go_to_add_member().add_member('18211111111').get_member_list()
        # assert "zh5" in result
        myreport = self.main.go_to_add_member().add_member(name).input_acctid(acctid).input_phone(phone).click_button()
        mydata = myreport.get_member_list1()
        print(f'实际结果：{mydata}')
        assert mydata == '保存成功'

    @pytest.mark.parametrize('name,acctid ,phone',get_contact()[0])
    def test_add_member_fail(self,name,acctid ,phone):
        # self.main.go_to_add_member().add_member('sdadsad')
        myreport1 = self.main.go_to_add_member().add_member(name).input_acctid(acctid).input_phone(phone).click_button()
        # result = AddMember(self.main._driver).get_phone_error_messrge()
        #进行实例化，并拿到报错信息
        mydata1 = myreport1.get_phone_error_messrge()
        print(f'实际结果:{mydata1}')
        assert mydata1 == '请填写正确的手机号码'
        #失败的用例,断言失败

    @pytest.mark.parametrize('department_name,file',get_contact()[2])
    def test_contact_add_member(self, department_name,file):
        # 1. 跳转到通讯录页面 2.添加部门 3.导入文件
        myreport2 = self.main.go_to_address_book().click_add().click_add_button().Enter_department_name(department_name).Subordinate_departments()\
            .Click_departments().click_confirm_button().click_import().click_File_to_import().click_Upload_file(file)
        mydata2 = myreport2.get_meber_list2()
        print(f'实际结果：{mydata2}')
        assert mydata2 == '通讯录批量导入.xlsx'

    def teardown(self):
        self.main.base_quit()


