#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/28 14:59
# @Author  : taojian
# @Site    : 
# @File    : 2019.8.28_协程 async.py
# @Software: PyCharm

import asyncio
import time
#正常统计运行时间
# def crawl_page(url):
#     print('爬取{}'.format(url))
#     sleep_time=int(url.split('_')[-1])
#     time.sleep(sleep_time)
#     print('ok {}'.format(url))
#
# def main(urls):
#     for url in urls:
#         crawl_page(url)
# start = time.perf_counter()
# main(['url_1','url_2','url_3'])
# alltime=time.perf_counter()-start
# print(alltime)

#协程并发方式
async def crawl_page(url):
    print('爬取{}'.format(url))
    sleep_time=int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('ok {}'.format(url))

def main(urls):
    loop = asyncio.get_event_loop()
    tasks=(crawl_page(url) for url in urls)
    #asyncio.gather并发
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

if __name__ == '__main__':
    start = time.perf_counter()
    print(start)
    main(['url_1','url_2','url_3'])
    All_time=time.perf_counter()-start
    print('Wall_time:{:.2f}'.format(All_time))
