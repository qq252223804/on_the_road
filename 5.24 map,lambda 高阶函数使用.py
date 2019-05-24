#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: 5.24 map,lambda 高阶函数使用.py
@time: 2019/5/24 15:08
@software: PyCharm
"""

# map(function, iterable, ...)
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数，
# 返回包含每次 function 函数返回值的新列表。
def f(x):
    return x*x
print (list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#lambda 匿名函数 更快
print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))  # 使用 lambda 匿名函数

#map zip 快速生成字典 {}更有优势
a=('lucy','dali','ajian')
b=(18,19,20)
c=dict(map(lambda x,y:(x,y),a,b))
d={x: y for x,y in zip(a,b)}
print(c)
print(d)



# upper 与lower使用
def format_name(s):
    s1=s[0:1].upper()+s[1:].lower()
    return s1
print (list(map(format_name, ['adam', 'LISA', 'barT'])))


