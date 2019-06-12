import pytest

'scope为function级别'
@pytest.fixture()
def first():
    print("\n获取用户名")
    a="nuo"
    return a
@pytest.fixture(scope="function")
def second():
    print("\n获取密码")
    b="123455"
    return b

def test_1(first):
    '''用例传fixture'''
    print("测试账号：%s"%first)
    assert first=="nuo"

def test_2(second):
    '''用例传fixture'''
    print("测试密码：%s"%second)
    assert second=="123455"

if __name__ == '__main__':
    pytest.main(["-s","fixtureandscope.py"])
