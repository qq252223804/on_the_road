#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: taojian
@file: parse.py
@time: 2019/5/24 16:02
@software: PyCharm
"""
import re


# 你不用太关心这个函数
def parse(text):
    # 使用正则表达式去除标点符号和换行符
    text = re.sub(r'[^\w ]', '', text)
    print(text)


    # 转为小写
    text = text.lower()

    # 生成所有单词的列表
    word_list = text.split(' ')
    # print(word_list)

    # 去除空白单词
    #折行的空白字符得去掉
    word_list = filter(None, word_list)


    # 生成单词和词频的字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    print(word_cnt)

    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_cnt


with open('in.txt', 'r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('out.txt', 'w') as a:
    for word, freq in word_and_freq:
        a.write('{} {}\n'.format(word, freq))


