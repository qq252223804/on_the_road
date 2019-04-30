# -*- coding: utf-8 -*- 
# @Time : 2018/11/29 14:40 
# @Author : taojian 
# @File : 11.29_json文件读写.py

import json
#dumps：将python中的 字典 转换为 字符串
user_dict1={"data1":{"用户名": "gang","年龄": 18,"城市": "上海"}}
user_dict2={"data2": {"编写人": "taojian"}}
#字典不能相加 只能update
user_dict1.update(user_dict2)
user_json = json.dumps(user_dict1,ensure_ascii=False,indent=4)  # 将生成的dict转换成str
# print(type(user_json))


# dump: 将数据写入json文件中
# a 追加写入，wb,覆盖写入
with open("E:\\在路上\\users\\gang.json",'wb') as file:    #打开写入不能使用w了 因为为二进制 用wb
	file.write((user_json).encode('utf-8'))        #json文件写入中文 需加encode编码


	
# load:把文件打开，并把字符串变换为数据类型
with open("E:\\在路上\\users\\gang.json",'r',encoding='utf-8') as load_f:   #json文件包含中文 则打开需标明
	load_dict =json.load(load_f)
	print(load_dict.get('data'))
	print(load_dict.get('data1'))
