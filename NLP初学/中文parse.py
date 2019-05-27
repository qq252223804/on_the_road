#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: 中文parse.py
@time: 2019/5/24 16:15
@software: PyCharm
"""

import re

def parse1(text):
    # 使用正则表达式去除标点符号和换行符

    text=re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[:：+——()?【】“”！，。？、~@#￥%……&*（）]+", "", text)
    # 按照词频排序


    word_cnt = {}
    for word in text:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    print(word_cnt)

    #返回出文字出现的频率 以数字进行倒叙排序 reverse
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_cnt

with open('in1.txt', 'r', encoding='UTF-8') as fin:
    text = fin.read()

a=parse1(text)
print(a)

with open('out1.txt', 'w') as b:
    for word, freq in a:
        b.write('{} {}\n'.format(word, freq))
