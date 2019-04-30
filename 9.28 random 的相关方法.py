#coding:utf-8
import random
import string
import time

print([item for item in dir(random) if not item.startswith(('__'))])


#整型的伪随机数
print(string.ascii_letters)  #所有字母
print(string.digits)         #所有的一位数

#random.randint()随机生一个整数int类型
print(random.randint(1,10))

#random.choice(seq) 从序列seq中返回随机的元素；
buf=['@163.c0m','@qq.com','@email.com','@yahu,com']
print(random.choice(buf))

# random.sample(seq, n) 从序列seq中选择n个随机且独立的元素；
head=random.sample(string.ascii_letters+string.digits,16)
numbers=list(string.digits)
print(head)
print(numbers)

#生成邮箱前缀
#'分隔符'.join 快速的把一个列表/元组转换成字符串
email=''.join(head) + random.choice(buf)
print(email)

#生成随机手机号
mobile=['130','132','150','155','177','186']
print(random.choice(mobile) + str(random.randint(10000000,99999999)))
print(random.choice(mobile)+''.join(random.sample(numbers,8)))
# random.sample()可以从指定的序列中，随机的截取指定长度的片断，不作原地修改。



#生成随机的8位随机密码
mima=random.sample(string.ascii_letters+string.digits,8)
print(''.join(mima))

# mobiles=[]
# def random_mobile(i):
# 	while i<=10:
# 		i+=1
# 		str= ['130', '132', '150', '155', '177', '186']
# 		mobile=random.choice (str) + ''.join (random.sample (list(string.digits), 8))
# 		mobiles.append(mobile)
# 	return mobiles
# phone=random_mobile(i=1)
# print(phone)

times=str(round(time.time()*1000))
print(times)
b=times[5:13]
print(b)

