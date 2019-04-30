import os

import requests
import json

#
api_url='https://api.douban.com/v2/movie/top250'
result=requests.get(api_url).json()   #返回字典类型
# result2=json.dumps(result)   #将dict-str
print(type(result))
print(result)
# print(result2)
#字典中取值     用.get 且可以多次使用

data=result.get('subjects')
print(data)

#生成一条条可迭代对象
ziyuan=[]
for item in data:
	#列表中，字典取值用[]
	# print(item)
	# print(item['rating'],item['genres'])
	print(str(item['rating'])+str(item['genres']))

	print(item['title'])
	print(item['alt'])
	# ziyuan.append(item['rating'])
	# ziyuan.append(item['genres'])
	# ziyuan.append(item['title'])
	# print(ziyuan)
	# print("+"*100)
	with open(os.getcwd() + "\\douban_movie\\" + "1.txt", "a+", encoding='utf-8')  as f:

		f.write(str(item['rating'])+str(item['genres'])+'\n')
		f.write(str(item['title']) + '\n')
		f.write(str(item['alt']) + '\n')
		f.write(str("+"*100)+ '\n')
		f.close()

		

		


	



