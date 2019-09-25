from random import randint

student_info={'studernt%d'%i: randint(80,100) for i in range(1,21)}

print(student_info)

# 字典解析
print({k:v for k,v in student_info.items() if v>=90})

g=filter(lambda item:item[1]>=90,student_info.items())

# 对于构造器g生成不同格式数据
print(dict(g))
g=filter(lambda item:item[1]>=90,student_info.items())
print(list(g))