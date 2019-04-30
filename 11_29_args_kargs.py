#注意点：参数arg、*args、**kwargs三个参数的位置必须是一定的。
# 必须是(arg,*args,**kwargs)这个顺序，否则程序会报错。

# ** kwargs
# 打包关键字参数成dict给函数体调用

# *args
# 用来将参数打包成tuple给函数体调用
def function(arg,*args,**kwargs):
    print(arg,args,kwargs)

function(6,7,8,9,a=1, b=2, c=3)