#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author:p
# Datetime:2019/9/16 16:38
# File: 2019_9_16sort 与sorted.py
"""

"""
# 1.使用sort排序
# 使用sort()方法对list排序会修改list本身,不会返回新list，通常此方法不如sorted()方便，但是如果你不需要保留原来的list，此方法将更有效sort()。

# sort()不能对dict字典进行排序

my_list = [3, 5, 1, 4, 2]
my_list.sort()
print(my_list)


# 2.使用sorted()排序
my_list = [3, 5, 1, 4, 2]
result = sorted(my_list)
print(result)

#list 进行排序
students = [('john', 'A', 10), ('jane', 'B', 16), ('dave', 'C', 15)]

print(sorted(students, key=lambda s: s[2])) #升序
print(sorted(students, key=lambda s: s[1],reverse = True )) #降序

#dict 进行排序 必须先将dict进行items处理 转为list 然后按key 或者value进行排序
# Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
my_dict = {"a":"1", "c":"3", "b":"2"}
# print(my_dict.items())
result2 = sorted(my_dict.items(), key=lambda x:x[0],reverse=False)
print(dict(result2))


#对str进行排序
# reverse=False为正序，True为反序
str='3215687AbcBdeC'
str2=''.join(sorted(str))
str3=''.join(sorted(str,reverse=True))
print(str2)
print(str3)

# 使用json方式对字典进行排序
import json
dict={"c":"3", "b":"2", "a":"1"}
dict1=json.dumps(dict,sort_keys=True)
print(dict1)
json_str='{"c":"3", "b":"2", "a":"1"}'
json_str1=json.loads(json_str)
print(json.dumps(json_str1,sort_keys=True))
# new_str= sorted(dict.items(), key=lambda x:x[0])
# print(new_str)