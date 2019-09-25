#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: 5.24 map,lambda upper()使用.py
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


# map(func,parmters)
# upper 与lower使用
def list_toUpper(s):
    # print(s[0:1],s[1:])
    s1=s[0:1].upper()+s[1:].lower()
    return s1
print (list(map(list_toUpper, ['adam', 'LISA', 'barT'])))

def str_toUpper(str):
    #将句子使用split切割为list数组
    split_list=str.split()
    # 遍历列表长度值
    for i in range(len(split_list)):
        # 使用capitalize()函数将每个单词首字母转为大写
        split_list[i]=split_list[i].capitalize()
        # 使用join将列表转为字符串

    split_list=" ".join(split_list)
    return split_list
content="hello world"
print(str_toUpper(content))