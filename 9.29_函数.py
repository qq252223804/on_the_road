#coding:utf-8
import random
import string
import json


if __name__=='__main__':
	#function 代表函数，method代表方法
	#function不需要与任何 类对象绑定
	#method一定会绑定衣蛾对象 cls、self
	def hi(name):
		"""
		:param name:这是一个用户名
		:return:
		"""
		print('hi {}'.format(name))
	hi('zhangsan')
	def mobile():
		"""
		   doc string 函数的注释内容
		:return:
		"""
		# print('numbers:{}'.format(st))
		numbers=list(string.digits)
		# shuffle()方法将序列的所有元素随机排列
		random.shuffle(numbers)
		headers=['130','132','150','155','177','186']
		mobile_number=random.choice(headers) + ''.join(random.sample(numbers,8))
		print(mobile_number)
		return mobile_number
	# mobile()
	

	def print_user_info(name,age,work,city='杭州'):
		"""
		 这个函数 接收三个参数 把他们拼接成一I句话 不做返回
		:param name:
		:param age:
		:param work:
		:return:
		"""
		print('我是{}，我今年{}，我的工作是{},我生活在{}'.format(name,age,work,city))
	name='taojian'
	age=25
	work='IT'    #定义好值  可传输入变量
	# print_user_info(name,age,work)
	
	def print_user_infos(*args,**kwargs):
		"""
		 *arges :arg类型是一个元组，他接受不确定个数  的非keywords类型参数
		 **kwargs kwargs类型是一盒字典，他接受不确定个数 的非keywords类型参数
		:param args:
		:param kwargs:
		:return:
		"""
		print(name)               #打印具体的值
		print(args,type(args))       #传入元组 则打印元组
		print(kwargs,type(kwargs))   #传入字典 则打印字典
	
	name = 'taojian'
	age = 25
	work = '软件测试'  # 定义好值  可传输入变量
	# print_user_infos(name,age,work,1,2,3,4,5,a=1,b=2)
	
	def get_user_info():
		"""
		  仅作返回变量信息
		:return:
		"""
		user_mobile=mobile()
		num=8  #生成几位邮箱前缀
		footer=['@163.c0m','@qq.com','@email.com','@yahu,com']
		header=''.join(random.sample(string.ascii_letters+string.digits,num))
		user_email=header+random.choice(footer)
		user_password=''.join(random.sample(string.ascii_letters+string.digits+string.punctuation,8)) #string.punctuation 所有标点符号
		return user_mobile,user_email,user_password
		
	def print_userinfo():
		"""
		  打印用户信息
		:return:
		"""
		user_mobile,user_eamil,user_password=get_user_info()      #导出函数中返回的字段
		print('当前用户手机号是：{},邮箱是：{},密码是:{}'.format(user_mobile,user_eamil,user_password))
	print_userinfo()
	
	
	def save_user_info():
		'''
		  保存生成的用户信息  随机保存三个
		:return:
		'''
		# result=[]
	
		try:
			with open('users/userinfos.txt',"a+",encoding='utf-8') as file:  #a+表示追加方式写入
				a = [{"sas": "sas"}, {"sad": "sad"}]
				file.write(str(a))         #将list 转为str 格式写入
			
			
				text = ('mobile', 'email', 'password')
				for num in range(3):    #一次写入三个
					userinfo = get_user_info()
					result = {key: value for key, value in zip(text, userinfo)}  # 字典推导式
					result_json = json.dumps(result, indent=4, ensure_ascii=False)    #将dict 转换成str 格式 写入txt文本
					file.write(result_json)
			
					print(type(result_json))
					print(result_json)

			return "数据存储完成"
		except Exception as e:
			print(e)
	
	
	save_user_info()

