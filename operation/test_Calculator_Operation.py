#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_Calculator_Operation
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/8/14 22:14
@Desc   ：
=================================================='''
import pytest
import yaml

from Homework.calculator import Calculator


def get_datas():
    with open('./clacul.yaml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]


def get_datas1():
    with open('./clacul.yaml', encoding='utf-8') as f1:
        mydata1 = yaml.safe_load(f1)
        subdata1 = mydata1['sub']['datas1']
        myids1 = mydata1['sub']['myids1']
    return [subdata1, myids1]


def get_datas2():
    with open('clacul.yaml', encoding='utf-8') as f2:
        mydatas2 = yaml.safe_load(f2)
        muldata2 = mydatas2['mul']['datas2']
        myids2 = mydatas2['mul']['myids2']
    return [muldata2, myids2]


def get_datas3():
    with open('./clacul.yaml', encoding='utf-8') as f3:
        mydatas3 = yaml.safe_load(f3)
        divdata3 = mydatas3['div']['datas3']
        myids3 = mydatas3['div']['myids3']
    return [divdata3, myids3]


class TestCalcu():

    def setup_class(self):
        self.calc = Calculator()
        print('setup_class: 开始计算')

    def teardown_class(self):
        self.calc = Calculator()
        print('teardown_class : 结束计算')

    @pytest.mark.parametrize('a,b,expect',
                             get_datas()[0],
                             ids=get_datas()[1]
                             )
    def test_add(self, a, b, expect):
        print('计算相加')
        results = round(self.calc.add(a, b), 2)
        assert expect == results
        print(results)

    @pytest.mark.parametrize('a,b,expect',
                             get_datas1()[0],
                             ids=get_datas1()[1]
                             )
    def test_sub(self, a, b, expect):
        print('计算相减')
        results = self.calc.sub(a, b)
        assert expect == results
        print(results)

    @pytest.mark.parametrize('a,b,expect',
                             get_datas2()[0],
                             ids=get_datas2()[1]
                             )
    def test_mul(self, a, b, expect):
        print('计算相乘')
        results = self.calc.mul(a, b)
        assert expect == results
        print(results)

    @pytest.mark.parametrize('a,b,expect',
                             get_datas3()[0],
                             ids=get_datas3()[1]
                             )
    def test_div(self, a, b, expect):
        print('计算相除')
        results = self.calc.div(a, b)
        assert expect == results
        print(results)
