# coding:utf-8
import random

import unittest
import requests
import warnings

from my_fake_useragent import UserAgent

print({"User-Agent": UserAgent().random()})
print({
    "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"})

# 这里登陆的方法不可放入class中 不然 unittest遇到test 命名的用例会执行一遍 后面用例调用login方法返回的内容又会登陆一遍
def test_login():
	"""
	仅作返回cookies
	:return:
	"""
	data = {"username": "18657738815", "password": 123456}
	url = "http://pre-admin.mofangcar.com/cms/login"
	headers = {"User-Agent":UserAgent().random()}
		# "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
	res = requests.post(url, data=data, headers=headers, verify=False)
	print(res.json())
	# print(res.text)
	# print(res.cookies['JSESSIONID'])  # 有的把cookie信息存在cookies中  有的放入返回的data中
	return res.cookies


class cmf_cms(unittest.TestCase):
	cookies = test_login()  # 将登陆后的cookies设置为全局变量 这样只需要一次登陆即可
	def setUp(self):
		# self.session = requests.Session()  # 类的实例化 后面用例不用一一执行了

		warnings.filterwarnings("ignore")

	def tearDown(self):
		pass


	def test1_post_demo(self):
		"""
		添加仓库
		:return:
		"""
		i=random.randint(1,1000)
		data={"name":"杭州%s库"%i,
			"type":2,
			"deptId":7,
			"provinceCode":330000,
			"cityCode":330100,
			"address":"浙江省杭州市江干区彭埠镇",
			"cmsSysUserId":"5b483c19e21b840001220f72",
			"phone":18657738815}

		url="http://pre-admin.mofangcar.com/cms/purchaseSales/createCarWarehouse"
		res=requests.post(url,data=data,cookies=self.cookies,verify=False)
		self.assertEqual(res.status_code,200)
		print(res.json())

	def  test2_get_demo(self):    #get方法也可采取dict方法传入 但参数采取 params或者直接将参数放入url中
		"""
		查询购车申请待处理订单——按手机号
		"""

		data = {
			"page":1,"limit":20,"keyword":18657738815,
			"apply_type":"","city_code":"","begin_date":"","end_date":""
		}

		url="http://pre-admin.mofangcar.com/cms/carApply/getPendingList"

		res=requests.get(url,params=data,cookies=self.cookies,verify=False)
		self.assertEqual(res.status_code, 200)
		print(res.json())




if __name__=="__main__":
	unittest.main()

	pass

