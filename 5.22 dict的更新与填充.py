#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: 5.22 dict的更新与填充.py
@time: 2019/5/22 11:50
@software: PyCharm
"""

# 字典更新
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

# 字典填充
C = {}
C['id'] = 1
C['NAME'] = 'lucy'
print(C)

# 列表与字典相互转换
# encoding=utf-8
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
F = dict(zip(list1, list2))
print(F)

# 两个字典之间结合
# 更新后的放前面
C.update(F)
print(C)
print(F)

# 获取字典中的key 生成列表
# 获取字典中的value 生成列表

key_list = list(C.keys())
key_value = list(C.values())
print(key_list)
print(key_value)


#
# arr=[{"city":"上海","area":"浦东"},{"city":"上海","area":"浦西"},
#      {"city":"杭州","area":"上城"},{"city":"杭州","area":"下城"}]
# # arrs=[{"city":"","areas":[]}]
# # arrss=[{"city":"","areas":[]}]
# # for i,j in zip(arr,range(arr.__len__())):
# #     if arr[j]["city"]=="上海":
# #         arrs[0]["city"]=i["city"]
# #         arrs[0]["areas"].append(arr[j]["area"])
# #     if arr[j]["city"]=="杭州":
# #         arrss[0]["city"]=i["city"]
# #         arrss[0]["areas"].append(arr[j]["area"])
# # arrs.extend(arrss)
# # print(arrs)
# arr_set=set()
# arr_list=[]
# for i in arr:
#     arr_set.add(i["city"])
#
# #第一层循环城市
# for i in arr_set:
#     arr_dict = {}
#     area_list = []
#     #第二层循环地域
#     for j in arr:
#         if i==j["city"]:
#             #字典的key赋值
#             arr_dict["city"] = i
#             arr_dict.setdefault("areas",[]).append(j["area"])
#             # area_list.append(j["area"])
#     # 字典的areas赋值 list的列表
#     # arr_dict["areas"]=area_list
#     arr_list.append(arr_dict)
# print(arr_list)


# a={}
# for i in range(3):
#     a.setdefault("citt",[]).append(i)
# print(a)


list=[{"天虹":1000},{"天虹":200},{"长城":2000},{"景顺":500},{"景顺":100}]
arr_dict = {}
def check_list(list):
    for i in list :
        for product,price in i.items():
            if product in arr_dict:
                arr_dict[product]+=price
            else:
                arr_dict[product]=price
    new_arr_dict=sorted(arr_dict.items(),key=lambda x:x[0], reverse=True)
    return new_arr_dict
print(check_list(list))

# mobile=[['apple','ios',100,10],['pear','android',200,20],['apple','ios',500,50],['pear','android',600,60]]
# mobiledict={}
# for elem in mobile:
#
#     key=(elem[0],elem[1])
#     # print(key,elem[2])
#     if key in mobiledict:
#         # 打印字典的value值
#         print(mobiledict[key])
#         # 然后取第一个value 第二个value进行叠加
#         mobiledict[key][0]+=elem[2]
#         mobiledict[key][1]+=elem[3]
#     else:
#         mobiledict[key]=[elem[2],elem[3]]
# print(mobiledict)