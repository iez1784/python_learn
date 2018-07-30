# -*- coding: UTF-8 -*-
__author__ = 'zhangedison'

"""
请写出下列代码运行结果，并解释
"""

# X = 99
#
# def func():
#     print(X)
#     X = 88
#
# print(func())


"""
请写出下列代码运行结果，并解释
"""

import datetime,time

def func(now=datetime.datetime.now()):
    print(now)

func()

time.sleep(5)

func()



"""
请写出下列代码运行结果，并解释
"""

def func(a=[]):
    a.append(1)
    print(a)

func()
func()
func()