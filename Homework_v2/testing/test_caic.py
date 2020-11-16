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


# 读取测试数据
from Homework_v2.calculator import Calculator


class TestCalc:
    #     def setup_class(self):
    #         print("开始计算")
    #         self.calc = Calculator()
    # # setup_calss,teardown_calss 实例所有的用例
    #
    #     def teardown_class(self):
    #         print("结束计算")
    #         self.calc = Calculator()

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
    # @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    # @pytest.mark.fiaky(reruns=5)
    # @pytest.mark.run(order=2)#按照顺序执行用例
    def test_add(self, get_calc, get_data):
        # calc = Calculator()
        # 相加
        result = round(get_calc.add(get_data[0], get_data[1]), 2)
        # 使用round方法保留小数后两位
        print(f'相加等于 {result}')
        assert get_data[2] == result

    # @pytest.mark.run(order=1)
    @pytest.mark.sub
    def test_sub(self, get_calc, get_data1):
        # calc = Calculator()
        # 相除
        result = round(get_calc.sub(get_data1[0], get_data1[1]), 2)
        print(f'相相减等于 {result}')
        assert get_data1[2] == result

    # @pytest.mark.run(order=3)
    @pytest.mark.mul
    def test_mul(self, get_calc, get_data2):
        # calc = Calculator()
        # 相除
        result = round(get_calc.mul(get_data2[0], get_data2[1]), 2)
        print(f'相除等于 {result}')
        assert get_data2[2] == result

    # @pytest.mark.run(order=4)
    @pytest.mark.div
    def test_div(self, get_calc, get_data3):
        # calc = Calculator()
        # 相除
        result = round(get_calc.div(get_data3[0], get_data3[1]), 2)
        print(f'相除等于 {result}')
        assert get_data3[2] == result
