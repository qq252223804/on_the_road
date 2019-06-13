import pytest


class TestCase():
    @pytest.fixture(scope="module")
    def test_second(self):
        print("\n获取密码")
        b = "123456"
        return b
    @pytest.fixture(scope="module")
    def test_first(self):
        print("\n获取用户名")
        a = "nuo"
        return a
    def test_1(self,test_first):
        '''用例传fixture'''
        print("测试账号：%s"%test_first)
        assert test_first =="nuo"
    def test_2(self,test_second):
        '''用例传fixture'''
        print("测试密码：%s"%test_second)
        assert test_second=="123456"


if __name__ == '__main__':
    pytest.main(["-s","6-12-pytest.py"])
