
# 处理file 类型
# 返回path在当前系统的绝对路径
import os,time
times=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())
base_htmlpath=str(times)+'.html'

print(os.path.abspath('staff_info.txt'))
print(os.path.abspath(base_htmlpath))

# 判断path 对应文件或 目录是否存在，返回True或False
print(os.path.exists('C:\\Users\\p\\Desktop\\on_the_road\\NLP初学'))
print(os.path.exists('staff_info.txt'))

#返回path 中的目录名称
print(os.path.dirname('C:\\Users\\p\\Desktop\\on_the_road\\staff_info.txt'))
#返回path 中的最后的文件名称

# print(base_htmlpath)
print(os.path.basename('C:\\Users\\p\\Desktop\\on_the_road\\{}'.format(base_htmlpath)))