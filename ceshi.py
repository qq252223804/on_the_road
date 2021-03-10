#coding:utf-8
from login import Login
from login import oper




class Ceshi:

	def __init__(self):

		pass
	
	@staticmethod    #引用其他类的静态 方法 不需要标明self
	def get_DATA():
		data=Login(353,1).login1()
	
		print(data)
	
	@staticmethod
	def get_DATA2(Data):     #Data
		data = Login(66,1).login1()
		Data+=data
		print(Data)
	
	@staticmethod
	def get_DATA3():
		data=Login(6,1).login2()

		print(data)

Ceshi.get_DATA()
# Ceshi.get_DATA2(2)
# Ceshi.get_DATA3()
Login.ceshi()


# class pper:
# 	def __init__(self):
# 		print('pper chushihua')
#
#
# 	@staticmethod    #引用类 方法必须加静态方法
# 	def test_oper():
# 		print(oper(3,1).get_numm(True))
#
#
# pper().test_oper()



