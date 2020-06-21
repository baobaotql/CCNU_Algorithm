# -*- coding: utf-8 -*- 
# @Time : 2020/5/7 0:52 
# @Author : BaoBao
# @Mail : baobaotql@163.com 
# @File : add_threading.py 
# @Software: PyCharm

import threading

def thread_job():
    print('this is added Thread, number is %s'%threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job())
    added_thread.start()
    print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())


if __name__ == '__main__':
    main()