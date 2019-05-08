# coding:utf-8
import requests
from lxml import etree

import json


#
class BaseCrawl:
    def __init__(self):
        pass

    def request(self, url, encoding="utf-8"):
        response = requests.get(url)
        if response.encoding != 'utf-8':
            response.encoding = encoding  # 判断格式  不等于utf-8 就 赋值为utf-8
        return response.text

    def parse(self, html, xpaths):
        selector = etree.HTML(html)  # 类似选择器 进行解析对应xpath
        if isinstance(xpaths, (tuple, list)):  # 判断xpaths 类型
            return [selector.xpath(xpath) for xpath in xpaths]
        return selector.xpath(xpaths)

    def output(self, url, xpath):  # 不使用这个方法 因为会多次打开页面url
        html = self.request(url)
        return self.parse(html, xpath)


class Qiubai(BaseCrawl):  # 类的继承
    def __init__(self):
        super(Qiubai, self).__init__()  # 初始化超级类
        self.home_page_url = "https://www.qiushibaike.com/"
        self.html = self.request(self.home_page_url)


    def get_all_users(self):
        result = self.parse(self.html, '//h2/text()')
        # print(result)
        user_names = [item.strip('\n') for item in result]  # 去掉左右边\n
        return user_names

    # return json.dumps(user_names,ensure_ascii=False,indent=4 )

    def get_like_number(self):
        return self.parse(self.html, '//span[@class="stats-vote"]/i/text()')

    def get_user_content(self):
        selector = self.parse(self.html, '//div[@class="content"]')
        return [','.join(item.xpath('span/text()')) for item in selector]


if __name__ == "__main__":
    qb = Qiubai()
    # print(qb.get_all_users())
    users = qb.get_all_users()
    likes = qb.get_like_number()
    users_contents = qb.get_user_content()

    for user, like, content in zip(users, likes, users_contents):  # str.replace(old, new[, max])
        print("用户：{}\n发表了段子:{}\n一共有{}个用户喜欢\n".format(user, content.replace('\n', ',').strip(','), like))
