# 处理file 类型
# 返回path在当前系统的绝对路径
import os, time

times = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
base_htmlpath = str(times) + '.html'

print(os.path.abspath('staff_info.txt'))
print(os.path.abspath(base_htmlpath))

# 判断path 对应文件或 目录是否存在，返回True或False
print(os.path.exists('C:\\Users\\p\\Desktop\\on_the_road\\NLP初学'))
print(os.path.exists('staff_info.txt'))

print(os.path.basename('C:\\Users\\p\\Desktop\\on_the_road\\{}'.format(base_htmlpath)))

# os.path.abspath(__file__)求出文件所在的绝对路径
# 获取文件的当前py文件的目录
cur_path = os.path.dirname(os.path.abspath(__file__))
print(cur_path)
print(os.getcwd())

# 获得当前py文件的目录的上级目录,即cur_path的父级目录
parent_path = os.path.dirname(cur_path)
print(parent_path)
# 获取cur_path 父父级目录
parent_paths = os.path.dirname(parent_path)
print(parent_paths)

# 获取users 目录下的Raymon。json的路径
a = os.path.join(os.path.dirname(os.getcwd()), 'Common') + '\Raymon.json'
print(a)

b = 11
a = b
print("a=" + str(a))
