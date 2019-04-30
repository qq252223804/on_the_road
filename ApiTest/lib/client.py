

import requests
from fake_useragent import UserAgent    #随机生成头部信息库
import json


# @logger('requests封装')
class RunMain():
	# def __init__(self, url, method, data=None):  # 构造函数 就不用下面每次实例化了
	#     self.res = self.method_main(url, method, data)
	def __init__(self):
		self.headers={'User-Agent':UserAgent().random}
		print(self.headers)
	
	def GET(self, url,data,headers=None):  # get消息
		try:
			r = requests.get(url,data, headers=self.headers,verify=False)
			# r.encoding = 'UTF-8'
			# json_response = json.loads(r.text)  解码成str
			return r.json()
		except Exception as e:
			# LOG.info('get请求出错，出错原因:%s' % e)
			print('get请求出错,出错原因:%s' % e)
			return {}
	
	def POST(self, url, params,headers=None):  # post消息
		# data = json.dumps(params)
		try:
			r = requests.post(url,params=params, headers=self.headers,verify=False)
			
			return r.json()
		except Exception as e:
			# LOG.info('post请求出错，出错原因:%s' % e)
			print('post请求出错,原因:%s' % e)
	
	# def delfile(self, url, params):  # 删除的请求
	# 	try:
	# 		del_word = requests.delete(url, params, headers=self.headers)
	# 		json_response = json.loads(del_word.text)
	# 		return json_response
	# 	except Exception as e:
	# 		# LOG.info('del请求出错，出错原因:%s' % e)
	# 		print('del请求出错,原因:%s' % e)
	# 		return {}
	#
	# def putfile(self, url, params):  # put请求
	# 	try:
	# 		data = json.dumps(params)
	# 		me = requests.put(url, data)
	# 		json_response = json.loads(me.text)
	# 		return json_response
	# 	except Exception as e:
	# 		# LOG.info('put请求出错，出错原因:%s' % e)
	# 		print('put请求出错,原因:%s' % e)
	# 		return json_response
	
	def method_main(self, url, method, data=None, headers=None):
		respose = None
		if method == 'GET':
			respose = self.GET(url, data,headers=self.headers)
		else:
			respose = self.POST(url, data,headers=self.headers)
		return respose


if __name__ == '__main__':
	run = RunMain()  # 实例化
	url = 'http://pre-admin.mofangcar.com/cms/login'
	data ={"username": "18657738815", "password": 123456}
	
	respose = run.method_main(url, 'POST', data)
	# print (json.dumps(respose, indent=2, sort_keys=True))
	
	# print (type(respose))
	
	print(respose)
