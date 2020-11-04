#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Test_two -> utils
@IDE    ：PyCharm
@Author ：hang.zhao
@Date   ：2020/11/3 13:48
@Desc   ：
=================================================='''
import yaml



class Utils:
    #  load一个yaml文件，把数据读进来
    @classmethod
    def from_file(cls, path):
        with open(path,encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f) #  生成所有数据
            params = yaml_data['params'] # 取数据 有三项数据
            keys = set() # 定义一个集合，去重
            vlause = []
            if isinstance(params, list):
                #  每一行是个kv结构的字典
                for row in params:
                    if isinstance(row, dict):
                        for key in row.keys():
                            keys.add(key) #  取出所有的key,如果是多个参数是逗号隔开的
                            print(vlause)
                            vlause.append(list(row.values())[0])

            var_names=','.join(keys) # 取出参数化的名字,keys
            res = {'keys': var_names, 'values': vlause}
            print(res)
            return {'keys': var_names, 'values': vlause}

