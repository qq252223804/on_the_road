# -*- coding: utf-8 -*- 
# @Time : 2018/12/28 17:16 
# @Author : taojian 
# @File : 12.29_进阶习题.py


# 1.要求如下：给出以下购物列表，用户输入想要购买的物品，之后让用户输入想要购买该物品的数量，打印物品名、价格即数量。用户可循环输入
# msg_dic={
#     'iPhone':4000,
#     'apple':10,
#     'mac':8000,
#     'lenovo':3000,
#     'chicken':28
# }
# goods_l=[]
# while True:
#     for k in msg_dic:
#         print('NAME:<{name}> PRICE:<{price}>'.format(name=k,price=msg_dic[k]))
#     name=input('please input your goods name:').strip()
#     if len(name)==0 or name not in msg_dic:continue
#     while True:
#         count=input('please input your count:').strip()
#         if count.isdigit():break
#     goods_l.append((name,msg_dic[name],int(count)))
#     print(goods_l)
#


# 2.假设你想知道A的年龄，但你只知道A比B大2岁，B又比C大两岁，C又比D大两岁，D比E大两岁，恰好你知道E的岁数，那是不是就能知道A的岁数了呢，这就可以组成一个递归。那我们假设E的岁数是20
#    递归练习
# def age(n):
#     if n == 1:
#         return 20
#     else:
#         return age(n-1)+2
#
# print(age(5))


# def test(n):
#     if n == 0:
#         print("我的小鲤鱼",end="")
#     else:
#         print("抱着",end="")
#         test(n-1)
#         print("的我",end="")
# def func(n):
#     print('吓得我抱起了',end="")
#     test(n)
#
# func(3)


# yieid 用法
# all=20000
# def produce():
# 	"""生产衣服"""
# 	for i in range (1, all):
# 		yield "生产了第%s件衣服" % i
#
# product_g = produce ()
# print(next(product_g)) #要一件衣服
# print(next(product_g)) #再要一件衣服
# print(product_g.__next__()) #再要一件衣服
# num = 0
# for i in product_g:  # 要一批衣服，比如5件
# 	print (i)
# 	num += 1
# 	if num == 5:
# 		print ("一次批发了%s件衣服" % num)
# 		print("剩余%s件"%(all-num))
# 		break

#  yield from可以在实行for循环的效果的同时将代码变少：
# def gen1():
# 	for c in 'AB':
# 		yield c
# 	for i in range (3):
# 		yield i
# print (list (gen1 ()))

# # 简化后
def gen2():
	yield from '文婷婷'
	yield from '是傻逼'
	yield from range (3)
print(list(gen2()))

import re
a= 'not 404 found 张三 99 深圳'
list=a.split(" ")
print(list)
res=re.findall('\d+|[a-zA-Z]+',a)  #去除数字跟字母 中间加连接符
for i in res:
	if i in list:
		list.remove(i)
new_list=" ".join(list)
print(res)
print(new_list)