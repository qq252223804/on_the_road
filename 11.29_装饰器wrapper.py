#!/usr/bin/python
#coding=utf-8
# import functools
# def log(prefix, suffix):
#     def deco(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kargs):
#             print ('%s log start' % prefix)
#             print('get a is: %s' % args[0])
#             print('get b is: %s' % args[1])
#             print('get c is: %s' % args[2])
#             print('get d is: %s' % kargs['d'])
#             print('get d is: %s' % kargs['f'])
#             # 使用内嵌包函数的意思： func()=test 当test方式使用@log() 执行log，返回的deco
#             #再执行返回的deco 返回wrapper
#             #最终执行的wrapper    返回的是func 也就是内嵌包函数 调用装饰函数的同时 执行自己函数的功能
#              # @functools.wraps
#
#             func(*args, **kargs)
#             print ('%s log end' % suffix)
#         return wrapper
#     return deco

# @log('logstart', 'logend')
# def test(a, b, c, d, f):
#     print ('call func name is: %s' % test.__name__)
#
# test(1, 2, 3, d = 'dddd', f = 'ffff')

import time,random
# def cost_time(func):
#     def wrap(*args, **kwargs):
#         start_time = time.time()
#         print(start_time)
#         result = func(*args, **kwargs)    #基本装饰器函数，b=a(*args, **kwargs)   调用方法a_func=a 需返回a
#         print("cost time: {}".format(time.time() - start_time))
#         return result
#     return wrap
#
# @cost_time
# # 统计耗时的函数
# def a_func():
#     time.sleep(random.randint(1, 5))
#
# a_func()


#带参数的装饰器函数
# Python也支持带参数的装饰器，比如刚刚的cost_time加入一个报警机制，如果函数执行耗时大于3秒，就发出警告。
def cost_time(warn=3):
    def wrap(func):
        def in_wrap(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            cost = time.time() - start_time
            print("cost time: {}".format(cost))
            if cost > warn:
                print("warning, cost time is {} !!!".format(cost))
            return result
        return in_wrap
    return wrap

@cost_time()
def a_func():
    time.sleep(random.randint(1, 5))

a_func()

