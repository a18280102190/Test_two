# 创建conftest.py文件，加入如下代码，修改测试结果的编码格式
# conftest共享文件
# conftest.py用法
# 1.测试用例会优先读取当前模块下的fixture方法
# 2.其次读取当前目录下定义的conftest.py文件里面定义的fixture方法
# 3.如果当前文件或者当前目录没有，才会去项目目前下一层一层往上找
import os
from typing import List

import pytest
import yaml

from Homework_v2.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # 修改编码
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

# @pytest.fixture(scope='module')


@pytest.fixture(scope='session')
# scope = session 整个 session域只执行一次
def connDB():
    print('连接数据库')
    yield
    print('断开数据库')


# @pytest.fixture(scope="class")
@pytest.fixture(scope="module")
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")

#读取数据
def get_datas():
    # mydatapath = os.path.dirname(__file__)+"../datas/caic.yaml'"
    # with open(mydatapath, encoding='utf-8') as f:
    with open('../datas/caic.yaml', encoding='utf-8') as f:
        mydatas = yaml.safe_load(f)
        adddatas = mydatas['add']['datas']
        myids = mydatas['add']['myids']
    return [adddatas, myids]


@pytest.fixture(params=get_datas()[0], ids=get_datas()[1])
def get_data(request):
    return request.param


def get_datas1():
    with open('../datas/caic.yaml', encoding='utf-8') as f1:
        mydatas1 = yaml.safe_load(f1)
        suddatas = mydatas1['sub']['datas1']
        myids1 = mydatas1['sub']['myids1']
    return [suddatas, myids1]


@pytest.fixture(params=get_datas1()[0], ids=get_datas1()[1])
def get_data1(request):
    return request.param


def get_datas2():
    with open('../datas/caic.yaml', encoding='utf-8') as f2:
        mydatas2 = yaml.safe_load(f2)
        muldatas = mydatas2['mul']['datas2']
        myids2 = mydatas2['mul']['myids2']
    return [muldatas, myids2]


@pytest.fixture(params=get_datas2()[0], ids=get_datas2()[1])
def get_data2(request):
    return request.param


def get_datas3():
    with open('../datas/caic.yaml', encoding='utf-8') as f3:
        mydatas3 = yaml.safe_load(f3)
        divdata3 = mydatas3['div']['datas3']
        myids3 = mydatas3['div']['myids3']
    return [divdata3, myids3]


@pytest.fixture(params=get_datas3()[0], ids=get_datas3()[1])
def get_data3(request):
    return request.param
