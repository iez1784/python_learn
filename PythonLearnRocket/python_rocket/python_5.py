# -*- coding: UTF-8 -*-
__author__ = 'zhangedison'

"""
请写出下面代三运后后的结果，并解释原因
"""
def makeActions(N):
    acts = []
    for i in range(N):
        acts.append(lambda x: i ** x)
    return acts

acts = makeActions(5)
print("===makeAction===")
for act in acts:
    print(act(2))
print()

"""
第一题当中：
得到结果是：
16，16，16，16，16

makeActions函数中的lambda表达式，表头没有保存参数，函数体只有在调用的时候才会执行，才会去看是否有带参数，所以
acts的值都是[4**x, 4**x, 4**x, 4**x]
最后for act in acts中，act都传了一个x=2的值，所以结果都是4的平方，16

"""

def makeActions2(N):
    acts = []
    for i in range(N):
        acts.append(lambda x, i=i: i ** x)
    return acts


acts = makeActions2(5)
print("===makeAction2===")
for act in acts:
    print(act(2))
print()

"""
第二题当中，有保存传进参数 i=i，所以acts = [0的x方，1的x方，2的x方，3的x方，4的x方]
最后for act in acts中，传入参数i=2，所以结果是[0,1,4,9,16]
"""




