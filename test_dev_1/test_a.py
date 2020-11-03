import pytest


def func(x):
    return x + 1
#参数化，可以内部设置，也可以外部传入
@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (5,6)
])
def test_answer(a,b):
    assert  func(a) == b
@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (5,6)
])
def test_answer1(a,b):
    assert  func(a) == b


@pytest.fixture()#pytest装饰器
def login():
    username = 'jerrt'
    return username

class TestDemo:
    def test_a(self,login):
        print('登录操作')
        print(f"a username = {login}")#调用返回结果

    def test_b(self):
        print("b")

    def test_c(self,login):
        print(f"c  login = {login}")


if __name__ == '__main__':
    pytest.mian(['test_a.py::TestDemo','-v'])
