#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> test_caic
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/9 20:40
@Desc   ：
=================================================='''
import pytest
import yaml

from Homework.calculator import Calculator
#读取测试数据
def get_datas():
    with open('../datas/caic.yaml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas,myids]
def get_datas1():
    with open('../datas/caic.yaml',encoding='utf-8') as f1:
        mydatas1 = yaml.safe_load(f1)
        suddatas = mydatas1['sub']['datas1']
        myids1 = mydatas1['sub']['myids1']
    return [suddatas,myids1]

def get_datas2():
    with open('../datas/caic.yaml',encoding='utf-8') as f2:
        mydatas2 = yaml.safe_load(f2)
        muldatas = mydatas2['mul']['datas2']
        myids2 = mydatas2['mul']['myids2']
    return [muldatas,myids2]

def get_datas3():
    with open('../datas/caic.yaml',encoding='utf-8') as f3:
        mydatas3 = yaml.safe_load(f3)
        divdata3 = mydatas3['div']['datas3']
        myids3 = mydatas3['div']['myids3']
    return [divdata3,myids3]

class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()
# setup_calss,teardown_calss 实例所有的用例

    def teardown_class(self):
        print("结束计算")
        self.calc = Calculator()

    @pytest.mark.add  # 标识符
    # 进行参数化
    # @pytest.mark.parametrize('a,b,expect', [
    #     (1, 1, 2),
    #     (0.1, 0.1, 0.2),
    #     (0.1, 0.2, 0.3),
    #     (100, 200, 300),
    #     (0, 10, 10),
    #     (-1, -2, -3)
    # ], ids=['整数', '小数', '小数', '长整型数字', '为零', '最小'])
    # 使用ids对结果进行命名
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        # calc = Calculator()
        # 相加
        result = round(self.calc.add(a, b), 2)
        # 使用round方法保留小数后两位
        print(f'相加等于 {result}')
        assert expect == result

    @pytest.mark.sub
    @pytest.mark.parametrize('a,b,expect',get_datas1()[0],ids=get_datas1()[1])
    def test_sub(self,a,b,expect):
        # calc = Calculator()
        # 相除
        result = round(self.calc.sub(a, b),2)
        print(f'相相减等于 {result}')
        assert expect == result

    @pytest.mark.mul
    @pytest.mark.parametrize('a,b,expect',get_datas2()[0],ids=get_datas2()[1])
    def test_mul(self,a,b,expect):
        # calc = Calculator()
        # 相除
        result = round(self.calc.mul(a, b),2)
        print(f'相除等于 {result}')
        assert expect == result

    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect',get_datas3()[0],ids=get_datas3()[1])
    def test_div(self,a,b,expect):
        # calc = Calculator()
        # 相除
        result = round(self.calc.div(a, b),2)
        print(f'相除等于 {result}')
        assert expect == result