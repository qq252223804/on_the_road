#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: 5.22 dict的更新与填充.py
@time: 2019/5/22 11:50
@software: PyCharm
"""

#字典更新
D = {'one': 1, 'two': 2}

D.update({'three': 3, 'four': 4})  # 传一个字典
print(D)

D.update(five=5, six=6)  # 传关键字
print(D)

D.update([('seven', 7), ('eight', 8)])  # 传一个包含一个或多个元祖的列表
print(D)

D.update(zip(['eleven', 'twelve'], [11, 12]))  # 传一个zip()函数
print(D)

D.update(one=111, two=222)  # 使用以上任意方法修改存在的键对应的值
print(D)

#字典填充
C={}
C['id']=1
C['NAME']='lucy'
print(C)


#列表与字典相互转换
#encoding=utf-8
list1=["a","b","c"]
list2=[1,2,3]
F=dict(zip(list1,list2))
print(F)

#两个字典之间结合
#更新后的放前面
C.update(F)
print(C)
print(F)


#获取字典中的key 生成列表
#获取字典中的value 生成列表

key_list=list(C.keys())
key_value=list(C.values())
print(key_list)
print(key_value)


