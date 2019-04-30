#coding:utf-8
import requests
from bs4 import BeautifulSoup

def get_nums(blogs_des):
	split_str=blogs_des.split('-')[1].strip()
	print(split_str)
	# print(type(split_str))

	# final_res=int(split_str)
	# return final_res

def get_score(blog_id):
	res=requests.get("http://www.cnblogs.com/%s/mvc/blog/sidecolumn.aspx"%blog_id)

	html=res.content
	soup=BeautifulSoup(html,"html.parser")
	lis=soup.find_all(id="sidebar_scorerank")
	for item in lis:
		li_lists=item.find_all('li')
		# print(li_lists)
		for li_item in li_lists:
			# print(li_item.text)
	# 	print("-------")
			if u"积分" in li_item.text:
				score=get_nums(li_item.text)
				print(score)
			elif u"排名" in li_item.text:
				rank=get_nums(li_item.text)
				print(rank)
			else:
				print("error")
		


			


if __name__=="__main__":
	print(get_score('zhangfei'))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

