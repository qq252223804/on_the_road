#coding:utf-8
#dir 用法
dict_dir_list=dir(dict)
list_dir=dir(list)
print(dict_dir_list)
print(list_dir)
#列表推导式
dict_module=[item for item in dict_dir_list if '__' not in item]
list_module=[item1 for item1 in list_dir if '__' not in item1]
print(dict_module)
print(list_module)
#字典推导式
list1 = ['name', 'age', 'sex']
list2 = ['kyda', 19, 'man']

ID = {x: y for x, y in zip(list1, list2)}
print(ID)
for tmp in ID.items():
	print(tmp)

#str yu list  dict
a =[{"sas": "1"}, {"sad": "2"}]
b=str(a)
# print(b)              #将list转变成str
# print(list(b))        #将str 变为list
c=[1,2,3,4]
d=[]
for key in a:

	print(key) #字典格式
	print(key.keys())
	print(key.values())     #字典的键与值
	c.extend(key)
	# extend()拓展列表，批量写入
	d.append(key)

print(c)
print(d)       #列表格式



# list1=['a','s','sd']
# print(''.join(list1))  #'分隔符'.join 快速的把一个列表/元组转换成字符串


#set yu list
# a_list=sorted([1,2,2,2,3,4,5,2])
# set_a_list=set(a_list)  #将list变为set 集合类型  且进行去重
# print(set_a_list)
# b_list=list(set_a_list)  #将set变回list 类型
# print(b_list)
#
# new_b_list=sorted(list(set(a_list)))
# print(type(new_b_list),new_b_list)
#
# # remove_b_list=new_b_list.remove(2)    remove 不做返回 赋值变量是不存在的
# # print(remove_b_list)
# new_b_list.remove(2)
# print(new_b_list)

# 列表和元组也可以运用双重推导（笛卡尔积）来创建。比如我们要生成一个二维坐标数组：
# coordinate = [(x, y) for x in range(2)
#               for y in range(2)]
# print(coordinate)
#



