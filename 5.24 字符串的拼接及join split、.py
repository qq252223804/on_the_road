#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: 5.24 字符串的拼接及join split、.py
@time: 2019/5/24 14:50
@software: PyCharm
"""

#+法 拼接
p=''
for n in range(0,10000):
    p+=str(n)
print(p)


#join 拼接
l=[]
for n in range(0,10000):
    l.append(str(n))
l=''.join(l)
print(l)

#map 快速拼接 最好使用
print(''.join(map(str,range(0,10000))))

#split 的运用

path='https://abs/index.html'
def query_data(namespace,html):
    return namespace,html
namespace=path.split('//')[1].split('/')[0]
html=path.split('//')[1].split('/')[1]
data=query_data(namespace,html)
print(data)

#split 将字符串快速分割成一个列表
a='I have a dream that my four little children'
b=a.split(' ')
print(b)