#coding:utf-8


class Human(object):
	"""
	人类
	"""
	
	#类的成员变量
	nb_leg=2     # 两只腿
	nb_hand=2    #两只手
	
	history=[0]
	
	def __init__(self,height,weight):
		self.height=height
		self.weight=weight
	def out_put_info(self,man):
		print("身高：%s,体重：%s" %(self.height,self.weight))
		print("%s只手,%s只脚 " %(self.nb_hand,self.nb_leg))
		print("history:%s"%self.history)
		
		if man==True:
			
			self.__private()
			print("大头：%s个，眼睛：%s个"%(self.head,self.eye))
		else:
			print("非正常人")
		
	
	#如果在一个方法前面加两个下划线，则此方法会变为私有方法，
	# 私有方法不能直接调用，必须构造另一个函数来调用私有方法,
    #私有方法的作用就是在开发的过程中保护核心代码。
	def __private(self):
		self.head=1
		self.eye=2


def human_demon():
	jim=Human(170,50)
	jim.nb_hand=3       #静态变量（类的数据属性） 对象调用类成员变量 并改变
	jim.out_put_info(True)
	print("++++++++++++++")
	print("human has %s hand" %Human.nb_hand)
	Human.nb_hand=8     #成员变量可改变
	lili=Human(190,80)
	lili.history.append(5)
	lili.out_put_info(False)

	
	# Human.__private()  #私有属性无法调用，只能类内部调用


#父类子类继承
class Person(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender



class Student(Person):
	def __init__(self, name, gender, score):
		super(Student, self).__init__(name, gender)
		self.score = score
	def __str__(self):
		return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)

s = Student('Bob', 'male', 88)
print (s)
	
if __name__=="__main__":
	human_demon()

	