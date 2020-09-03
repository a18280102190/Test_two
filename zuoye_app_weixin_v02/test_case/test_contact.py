#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_contact
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/9/1 15:45
@Desc   ：
=================================================='''
import pytest
import yaml

from zuoye_app_weixin_v02.page.app import App



def get_contact():
    with open("../datas_1/contacts.yaml",encoding='utf-8') as f:
        datas1 = yaml.safe_load(f)
        add_members = datas1['addname']
        del_members = datas1['delname']
    return [add_members,del_members]


class TestWeiXin():

    def setup(self):
        """
        启动app

        """
        self.app = App()
        self.main = self.app.start().goto_main()
        pass

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum',get_contact()[0])
    def test_addcontact(self,name,gender,phonenum):

        mypage = self.main.goto_addresslist().add_member().addmember_menual().edit_name(name).edit_gender(gender)\
            .edit_phonenum(phonenum).click_save()

        mytoast = mypage.get_toast()
        print(f'实际结果:{mytoast}')
        assert mytoast == '添加成功'

    @pytest.mark.parametrize('name1',get_contact()[1])
    def test_deletecontact(self,name1):
        print(f'成员ID：{name1}')
        mydelete = self.main.goto_addresslist_1().select_name().clickedeitbutton().editmember().deletename().confirm()\
            .search().search_name_id(name1)

        myresults = mydelete.get_results()
        print(f'实际结果：{myresults}')
        assert myresults == '无搜索结果'

