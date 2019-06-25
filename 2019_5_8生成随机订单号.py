#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: 2019_5_8生成随机订单号.py
@time: 2019/5/8 12:52
@software: PyCharm
"""
# 1.uuid方式
import time
import uuid


uid=uuid.uuid1()
print(len(''.join(str(uid).split('-'))))
suid =''.join(str(uid).split('-'))[0:27]
print(suid)


# 2.时间戳方式

order_no = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))+ str(time.time()).replace('.', '')[-7:]
print(len(order_no))

print(str(time.time()).replace('.', ''))