

class Login:
	def __init__(self,name=0,pawd=0):
		self.name = name
		self.pawd =pawd
		print('初始化name')

	def login1(self):
		res=self.name+self.pawd
	
		return 	res

	def login2(self):
		res = self.name - self.pawd
		return res
		
		
	@staticmethod    #引用本类中方法不需要 标明self
	def ceshi():
		A=Login(3,1).login1()
		print(A)
		B=Login(3,1).login2()
		print(B)
# Login.ceshi()
class oper:
	def __init__(self,name=None,id=None):
		self.name = name
		self.id =id
		self.numm=name+id


	def get_numm(self,numm):
		'''
		 输入numm 判断函数
		:param numm:
		:return:
		'''
		NUMM =0
		if numm==True:
			NUMM=self.numm
			return NUMM
		return NUMM

# A=oper(3,1).get_numm(True)
# print(A)
