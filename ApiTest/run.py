#coding:utf-8

import unittest
from BeautifulReport import BeautifulReport




if __name__=='__main__':
	suit=unittest.defaultTestLoader.discover('tests',pattern='test_*.py')
	report=BeautifulReport(suit)
	report.report(filename='测试报告',description='测试单接口报告',log_path='report')