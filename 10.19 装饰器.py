#coding:utf-8
import time

print("准备编写装饰器")

def set_log(func):
    print("装饰器顶层代码")
    def wrap(*args, **kwargs):
        print("装饰器内层代码")
        return func(*args, **kwargs)
    # time.sleep(4)
    print("准备返回wrap对象")
    return wrap

print("准备编写demo函数")

@set_log
# demo = set_log(demo)  语法糖等同于
def demo():
    print("正在运行demo函数")

if __name__ == '__main__':
    print("准备运行demo函数")
    demo()

'''
例如登陆功能
'''
# '''''示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
# 但发现新函数只在第一次被调用，且原函数多调用了一次'''
# def deco(func):
# 	print("before myfunc() called.")
# 	func()
# 	print("  after myfunc() called.")
# 	return func
# @deco
# def myfunc():
# 	print(" myfunc() called.")

#
# myfunc()
# '''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
# 内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
# '''
#
# def deco(myfunc):
# 	def _deco():         #假设为登陆方法
# 		print("before myfunc() called.")
# 		if True:          #如果登陆状态正确
# 			print("myfunc()方法执行时为登陆状态")
# 		else:
# 			print("重新跳转deco()登陆方法")
#
# 		print("  after myfunc() called.")
#
# 		myfunc()        #使用内嵌包函数保证了 使用语法糖的函数同时自己也被调用验证
#
# 	# 不需要返回func，实际上应返回原函数的返回值
# 	return _deco
# @deco
# def myfunc():
# 	print("登陆成功 可以进行return")
# 	return '执行myfunc方法的后续功能'
# # #
# myfunc()


# '''示例5: 对带参数的函数进行装饰，
# 内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
# '''
# def deco(func):
# 	def _deco(a, b):
# 		ret = func(a, b)    #给出ret值
# 		print("before myfunc() called.")
# 		print("  after myfunc() called. result: %s" % ret)
# 		func(a, b)
# 		return ret
#
# 	return _deco
# @deco
# def myfunc(a, b):
# 	print(" myfunc(%s,%s) called." % (a, b))
# 	return a + b+11
#
# myfunc(1,2)

# '''''示例6: 对参数数量不确定的函数进行装饰，
# 参数用(*args, **kwargs)，自动适应变参和命名参数'''
#
# def deco(func):
# 	def _deco(*args, **kwargs):
# 		print("before %s called." % func.__name__)
# 		ret = func(*args, **kwargs)
# 		print("  after %s called. result: %s" % (func.__name__, ret))
# 		return ret
#
# 	return _deco
#
# @deco
# def myfunc(a, b):
# 	print(" myfunc(%s,%s) called." % (a, b))
# 	return a + b
#
#
# @deco
# def myfunc2(a, b, c):
# 	print(" myfunc2(%s,%s,%s) called." % (a, b, c))
# 	return a + b + c
#
#
# myfunc(1, 2)
# myfunc2(1, 2, 3)

# '''''示例7: 在示例4的基础上，让装饰器带参数，
# 和上一示例相比在外层多了一层包装。
# 装饰函数名实际上应更有意义些'''
# def deco(arg):
# 	def _deco(func):
# 		def __deco():
# 			print("before %s called [%s]." % (func.__name__, arg))
# 			func()
# 			print("  after %s called [%s]." % (func.__name__, arg))
#
# 		return __deco
#
# 	return _deco
#
# @deco("mymodule")
# def myfunc():
# 	print(" myfunc() called.")
#
#
# @deco("module2")
# def myfunc2():
# 	print(" myfunc2() called.")
#
#
# myfunc()