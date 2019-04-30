#coding:utf-8

import qrcode

class StaffCard(object):
	"""
	员工名片
	"""
	
	def __init__(self,name,phone):
		self.name=name
		self.phone=phone
		
	def gen_vcard(self,file_path):
		template="BEGIN:VCARD\nFN:%s\nTEL:%s\nEND:VCARD"\
					%(self.name,self.phone)
		print(template)
		img=qrcode.make(template)
		img.save(file_path)
		

	
def gen_staff_info():
	"""
	生成50个员工信息，保存到文件中
	:return:
	"""
	name_list = open("name_list.txt", "w", encoding='utf-8')
	for i in range(100):
		name = "tao%s" % i
		phone = "1861234%04d" % i   ##%04d 表示:在输出整数x的时候 按照4个位子的空间左对齐 多余的位子用0代替
		str = "%s,%s\n" % (name, phone)
		name_list.writelines(str)
	name_list.close()
	
	
def gen_staff_info_qrcode():
	"""
	给100个员工 生成二维码 批量自动化
	:return:
	"""
	#读取文件
	staff_info=open("name_list.txt",'r',encoding='utf-8')
	for i in staff_info.readlines():
		# print(i)
	#解析文件
		name,phone=i.split(',')
		phone=phone.rstrip()
	#根据文件生成图片，并保存图片
		Vcards=StaffCard(name,phone)
		Vcards.gen_vcard('E:\\在路上\\qrcode_imgs\\'+'%s.png'%name)
		pass
	


if __name__=='__main__':
	
	# taojian=StaffCard("陶健","18657738815")
	# taojian.gen_vcard()
	gen_staff_info()
	gen_staff_info_qrcode()
	pass