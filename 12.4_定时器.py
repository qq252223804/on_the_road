# -*- coding: utf-8 -*- 
# @Time : 2018/12/4 12:00 
# @Author : taojian 
# @File : 12.4_定时器.py

# import datetime
# import time
#
#
# def doSth():
# 	print('test')
# 	# 假装做这件事情需要一分钟
# 	time.sleep(60)
#
#
# def main(h=0, m=0):
# 	'''h表示设定的小时，m为设定的分钟'''
# 	while True:
# 		# 判断是否达到设定时间，例如0:00
# 		while True:
# 			now = datetime.datetime.now()
# 			# 到达设定时间，结束内循环
# 			if now.hour == h and now.minute == m:
# 				break
# 			# 不到时间就等20秒之后再次检测
# 			time.sleep(20)
# 		# 做正事，一天做一次
# 		doSth()
#
# main()

# d1 = {'x': 1, 'y': 2, 'z': 3}
# for (k, v) in d1.items():
# 	print(k,v)

import datetime
import schedule
import threading
import time


def job1():
	print("I'm working for job1")
	time.sleep(2)
	print("job1:", datetime.datetime.now())


def job2():
	print("I'm working for job2")
	time.sleep(2)
	print("job2:", datetime.datetime.now())


def job1_task():
	threading.Thread(target=job1).start()


def job2_task():
	threading.Thread(target=job2).start()


def run():
	schedule.every(10).seconds.do(job1_task)
	schedule.every(10).seconds.do(job2_task)
	
	while True:
		schedule.run_pending()
		time.sleep(1)
		
run()
