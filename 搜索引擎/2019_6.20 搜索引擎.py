#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 20:06
# @Author  : taojian
# @Site    : 
# @File    : 2019_6.20 搜索引擎.py
# @Software: PyCharm

class SearchEngineBase():
    def __init__(self):
        pass
    def add_courps(self,file_path):
        '负责读取文件内容，将文件路径作为id，跟内容一同传给process_corpus'
        with open(file_path,'r') as a:
            text=a.read()
        self.process_corpus(file_path,text)

    def process_corpus(self,id,text):
        '文件路径为id ，处理后的text成为索引'
        raise Exception ('process_corpus 没有被完成')

    def search(self,query):
        '处理询问再通过索引检索 然后返回'
        raise  Exception('search 没有被完成')

# 继承
class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine,self).__init__()
        #初始化私有变量
        self.__id_to_texts={}

    #以下是继承的并重写的方法  其中add_courps无需重写 默认可调用
    def process_corpus(self,id,text):
        self.__id_to_texts[id]=text

    def search(self,query):
        results=[]
        for id ,text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results
def main(search_engine):
    for file_path in ['1.txt','2.txt','3.txt','4.txt','5.txt']:
        search_engine.add_courps(file_path)

    while True:
        query=input("input:")
        results=search_engine.search(query)
        print('found {}处 results:'.format(len(results)))
        for result in results:
            print(result)

searh_engine=SimpleEngine()
main(searh_engine)

