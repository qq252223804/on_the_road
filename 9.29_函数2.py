# coding:utf-8
import json


class PythonStudent:
    """
    这个类是python学员信息的存储类
    """

    def __init__(self, name, age, city):
        """
           这个类接受3个函数
        :param name:
        :param age:
        :param city:
        """
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        """
           save userinfo  字符类型为str
        :return:
        """
        titles = ('用户名', '年龄', '城市')
        userinfo = (self.name, self.age, self.city)

        user_dict = {key: value for key, value in zip(titles, userinfo)}
        user_json = json.dumps(user_dict, ensure_ascii=False, indent=4)  # 将生成的dict转换成str
        print(user_json)
        try:
            with open('users/{}.json'.format(self.name), "wb") as file:
                file.write(user_json.encode())  # dict 是无法进行encode 必须转换成str
            return "数据存储完成"
        except Exception as e:
            print(e)


class Crawl:
    """这是一个userinfo的展示类"""

    def __init__(self, url, xpath, craw_name):
        """
          初始化这个类，接受三个参数
        :param url: 请求的url
        :param xpath: 需要解析这个url的xpath
        :param craw_name: 爬虫的名字
        """
        self.info = url, xpath, craw_name

    def __repr__(self):
        """
           抽象方法
        :return:
        """
        print(dir(self))
        return '需要请求的url:{},对应解析xpath:{},爬虫对应的名字craw_name:{}'.format(*self.info)

if __name__ == '__main__':
    user_info = [
        ('gang', 18, '上海'),
        ('随便', 20, '俄罗斯'),
        ('Raymon', 28, '北京'),
        ('钩子', 50, '新加坡')
    ]
    for user in user_info:
        print(PythonStudent(*user))  # *表示取所有的参数内容！
    print(Crawl('127.0.0.1', '/cms/login', '登陆'))
