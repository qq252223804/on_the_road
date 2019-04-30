#coding:utf-8
import random

def count_staff():
	'''
	从花名册统计人数
	:return:
	'''

	try:
		staff_info_file=open('E:\在路上\staff_info.txt','r',encoding='utf-8')
		cnt=0
		cnt_female=0
		cnt_male=0
		for item in staff_info_file.readlines():
			# print(item)
			name,sex,age,phone=item.split(',')
			print('名字：%s，性别：%s，年龄：%s，手机号：%s'%(name,sex,age,phone))
			cnt +=1
			if sex =='F':
				# print(name)
				cnt_female+=1
			elif sex=='M':
				cnt_male+=1
			else:
				print('性别有误')
		print('公司有男士：%s人，有女生：%s人，总人数：%s' % (cnt_male, cnt_female, cnt))
		# print(cnt)
		staff_info_file.close()
	except Exception as e:
			print(e)

def count_staff_man():
	'''
	随机一个男生中奖
	:return:
	'''
	try:
		staff_info_file=open('E:\在路上\staff_info.txt','r',encoding='utf-8')
		cnt=0
		choose_list=[]
		for item in staff_info_file.readlines():
			name, sex, age, phone = item.split(',')
			if sex =='F':  #如果性别为女 则不加入这个姓名
				continue      #回到for循环
			choose_list.append(name) #如果没有if 则加入所有人的姓名
			choose_name=random.choice(choose_list)  #随机一个姓名
			cnt+=1
		print('程序运行了%s个周期'%cnt)
		print('所有候选人如下:\n%s'%choose_list)  #a/nb  表示a b直接换行
		print('找到一个男同学，名字为%s去给老板拿外卖' %choose_name)
	except Exception as e:
		print(e)
		
	
		
if __name__=='__main__':
	
	count_staff()
	count_staff_man()
	# staff_info_file=open('E:\\在路上\\11.txt','r',encoding='utf-8')
	#
	# for item in staff_info_file.readlines():
	# 	print(item)

