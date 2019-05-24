#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: 5.24 dict与sit的排序区别.py
@time: 2019/5/24 12:17
@software: PyCharm
"""


# #字典的排序
# ll={'b':1,'cc':6,'a':2}
# print(ll.items())
# dict_by_key=sorted(ll.items(),key=lambda x:x[0])#根据字典的键排序
# dict_by_value=sorted(ll.items(),key=lambda x:x[1])#根据字典的值 排序
# print(dict_by_key)
# print(dict_by_value)
#
# #集合的排序
# tt={3,4,2,1}
# print(sorted(tt))


# 打印出 1.有多少种水果 2.有多少种不同价格
products=[
    ('柠檬一级',80),
    ('柠檬二级',100),
    ('苹果',50),
    ('香蕉',30),
    ('橘子',50),

]

#以list方式循环
def find_product_price(products):
    unique_product=[]
    unique_price=[]
    for  product,price in products:  #A
        if product not in unique_product:#B
            unique_product.append(product)
        if price not in unique_price:
            unique_price.append(price)
    return unique_product,len(unique_product),len(unique_price)

print('unique product is() and count of unique product and price is {} '.format(find_product_price(products)))

# #以set 方式循环

def check_product_price(products):
    unique_product = set()
    unique_price = set()
    for product,price in products:
        unique_product.add(product)
        unique_price.add(price)
    for i in products:
        if max(unique_price) in i:
            print('最贵的水果及价格为:'+str(i))
    return unique_product,len(unique_product),len(unique_price)
#
# print('count of unique product and price is {} and {}'.format(check_product_price(products)[2],check_product_price(products)[3]))
# print('不同水果名称为:{}'.format(check_product_price(products)[1]))
# print('最贵的水果价格为：{}'.format(check_product_price(products)[0]))
print('unique product is() and count of unique product and price is {} '.format(check_product_price(products)))




