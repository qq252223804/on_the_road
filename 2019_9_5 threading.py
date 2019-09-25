import concurrent.futures
import requests
import threading
import time


# 并发
def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url) + '\n')


def download_all(sites):
    # print(map(download_one, sites))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_one, sites)


def main():
    sites = [
        'https://www.baidu.com/',
        'https://www.baidu.com/',
        'https://www.baidu.com/',
        'https://www.baidu.com/',
        'https://www.baidu.com/',
        'https://www.baidu.com/',
        'https://www.baidu.com/',
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))


if __name__ == '__main__':
    main()
