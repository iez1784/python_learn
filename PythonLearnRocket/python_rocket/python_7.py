# -*- coding: UTF-8 -*-
__author__ = 'zhangedison'

"""
1.       lambda 表达式和def语句有什么关系？

都是函数。
lambda：匿名函数，函数没有具体的名称，而用def创建的方法是有名称的。
python lambda会创建一个函数对象，但不会把这个函数对象赋给一个标识符，而def则会把函数对象赋值给一个变量。
python lambda它只是一个表达式，而def则是一个语句。lambda表达式运行起来像一个函数，当被调用时创建一个框架对象。

https://blog.csdn.net/u010159842/article/details/52982395

2.       比较 map, filter, reduce的异同

Python中map()、filter()、reduce()这三个都是应用于序列的内置函数
map(func, seq1[, seq2,…])
第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。

map没有看明白

filter函数：
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。


reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）
先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

3.       什么是函数注解，有什么作用？
函数注解是python3中新增加的特性。

函数注解语法 可以让你在定义函数的时候对参数和返回值添加注解

def foobar(a: int, b: "it's b", c: str = 5) -> tuple:
    return a, b, c
a: int 这种是注解参数
c: str = 5 是注解有默认值的参数
-> tuple 是注解返回值。

作用没有理解到，只做类型检查吗?
"""

