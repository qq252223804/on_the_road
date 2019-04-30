#coding:utf-8

#list  tuple string 切片取值
user_list=['钩子','gang','sisi','期盼','111','今晚打老虎']
#取出 列表中第2个 到第4个元素的全部值 list 0表示第一个
print(user_list[2:5])

user_tuple=('钩子','gang','sisi','期盼','111','今晚打老虎')
print(user_tuple[1:4])
#切片中 左边数字表示 1 第二个元素包含    4 第五个元素不包含

user_string_text='RayMond is good man'
print(user_string_text[4:7])
#每 2个 idnex 取一次值 0 2 4 6 8。。。
print(user_string_text[0::2])

#step 切片中的步长
number_list = [item for item in range(0,100)]
print(number_list)
print(number_list[0:50:2])
print(number_list[-2:-100:-2])
#切片的理解 list【起点:终点：每一步走多长】
