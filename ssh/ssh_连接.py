#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: ssh_连接.py
@time: 2019/4/30 12:05
@software: PyCharm
"""
import paramiko as paramiko
from ssh.Email import send_email

# 地址：https://blog.csdn.net/appke846/article/details/80514024
# 1 基于用户名和密码的 sshclient 方式登录
# 建立一个sshclient对象
ssh = paramiko.SSHClient()
# 允许将信任的主机自动加入到host_allow 列表，此方法必须放在connect方法的前面
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 调用connect方法连接服务器
ssh.connect(hostname='10.100.2.41', port=22, username='root', password='YH%6666!')
# 执行命令
stdin, stdout, stderr = ssh.exec_command('docker ps')
# 结果放到stdout中，如果有错误将放到stderr中
# print(stdout.read().decode())
# 关闭连接
lines=stdout.read().decode()

A='10.100.2.41/we_eat_bugs/loan-market-testing-qd'
B='10.100.2.41/we_eat_bugs/open-gateway-testing-qd'
C='10.100.2.41/we_eat_bugs/yyyq-app-bff-testing-qd'
def write_text(msg):
    with open('C:\\Users\\taojian\\Desktop\\on_the_road\\ssh\\msg.txt', "w", encoding='utf-8') as file:  # a+表示追加方式写入
        file.write(str(msg))  # 将list 转为str 格式写入

if A in lines :
    print('A ok')
else:
    send_email()
    write_text('loan-market-testing-qd服务挂了正在启动')
    raise Exception('check A')
if B in lines:
    print('B OK')
else:
    send_email()
    write_text('open-gateway-testing-qd服务挂了正在启动')
    raise Exception('check B')
if C in lines:
    print('C OK')
else:
    send_email()
    write_text('yyyq-app-bff-testing-qd服务挂了正在启动')
    raise Exception('check C')

