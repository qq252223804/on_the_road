#coding:utf-8
'''
获取字典中 子字典的对应值 以列表形式展现
取male 的第一个值
'''
from jsonpath_rw import jsonpath, parse
import re
#第一种    parse
# a = {"student":[
# 	{"male":176,"female":162},
# 	{"male":174,"female":159}
# 	]}
# b = parse("student[*].male")
# male=b.find(a)
# print(male)    #返回的是list,但是不是我们想要的值
# list=[match.value for match in male]
# print(list)
# print(list[0])



b={"student":[
	{"male":176,"female":162},
	{"male":174,"female":159},
	{"name":"tkjjjj"}
	]}
#第二种用for 迭代
# c=[]
# for item in b["student"]:
# 	c.append(item)
# print(c)
# print(c[0]['male'])

#列表推导式
d=[item for item in b["student"]]
print(d)
print(d[0].get('male'))


#第三种re.findall
# c=re.findall(r"'male': (\d+),",str(b))  #取数字
# d=re.findall(r"'name': '(.+?)'",str(b))     #取字母
# print(str(b))        #打印出来注意空格
# # print(c)
# print(c[0])
# print(d[0])

