#coding：utf-8


class Date(object):
	
	def __init__(self, day=0, month=0, year=0):
		self.day = day
		self.month = month
		self.year = year


	@classmethod
	def from_string(cls, date_as_string):
		day, month, year =(date_as_string.split('-'))
		date1 = cls(day, month, year)
		print(date1)
		return date1

#如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。

# 而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。
class A(object):
	bar = 1
	
	def foo(self):          # 不构造为静态方法， 既可以通过类的命名空间调用，也可以通过实例调用
		return 'foo'
	
	@staticmethod     # 构造为静态方法后，既可以通过类的命名空间调用，也可以通过实例调用，即self
	def foo2():
		return 'foo2'
		
	def static_foo2(self):
		print(self.foo2())
		print(A.foo2())
		print(self.foo())
		print(A.foo(self))

	@staticmethod
	def static_foo():    #不需要传入任何参数，但要写类名调用
		print('static_foo')
		print(A.bar)
		A().foo()


# 	@classmethod
# 	def class_foo(cls):      #但需要传入cls
# 		print('class_foo')
# 		print(cls.bar)  # 调用类对象 不需要重新输入 A
# 		cls().foo()     # 调用类方法 不需要重新输入 A
#
#
# A.static_foo()
#
# A.class_foo()


if __name__ == "__main__":
	test=A()
	test.static_foo2()
	# test.static_foo()
	# date2 = Date.from_string('11-09-2012')
	# print(date2)

	
	