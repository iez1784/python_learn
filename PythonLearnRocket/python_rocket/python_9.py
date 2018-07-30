# -*- coding: UTF-8 -*-
__author__ = 'zhangedison'

a = [x*x for x in range(10)]   #列表表达式，得出的结果是 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print((x*x for x in range(10))) # 生成器，<generator object <genexpr> at 0x0000020B46460C50>
c = {x*x for x in range(10)} # 集合生成器， {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}， 集合是无序的
d = {x:x*x for x in range(10)} #字典生成器， {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


print(a)
print(c)
print(d)


R = range(3)
print(R) # range(0,3) ， 这里为什么不是 [0,1,2]呢
l1 = iter(R)
l2 = iter(R)

#iter 迭代器

print(next(l1)) # 0
print(next(l1)) # 1

print(next(l2)) # 0
print(next(l1)) # 2


M = map(abs,(0,1,2))

l3 = iter(M)
l4 = iter(M)

print(next(l3))
print(next(l3))

print(next(l4))
print(next(l3))

"""
0
1
0
2
0
1
2
"""