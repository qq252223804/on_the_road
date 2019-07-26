# -*- coding: utf-8 -*- 
# @Time : 2019/1/18 10:37 
# @Author : taojian 
# @File : 2019_1_18 dubbo.py

import dubbo_telnet
def coondoubble_data(Host,Port,interface,method,param):
    try:
        # 初始化dubbo对象
        conn = dubbo_telnet.connect(Host, Port)
        # 设置telnet连接超时时间
        conn.set_connect_timeout(10)
        # 设置dubbo服务返回响应的编码
        conn.set_encoding('gbk')
        conn.invoke(interface, method, param)
        command = 'invoke %s.%s(%s)'%(interface,method,param)
        return  conn.do(command)
    except:
        return  Exception
if __name__=="__main__":
    Host = '192.168.1.203'  # Doubble服务器IP
    Port = 28008  # Doubble服务端口
    interface = 'com.zrj.pay.trade.api.QueryTradeService'  # 接口
    method = 'tradeDetailQuery'  # 方法
    param = {"message": "HelloWorld"}  # 参数
    data=coondoubble_data(Host,Port,interface,method,param)
    print(data)

