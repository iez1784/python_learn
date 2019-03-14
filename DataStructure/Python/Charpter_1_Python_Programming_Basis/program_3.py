# _*_ codfing: utf-8 _*_
__author__ = 'zhangedison'

"""
一个标准的科学实验是: 抛球并且看它能够弹跳多高。
一旦球的"弹跳性"已经确定了，这个比率值就会给出弹跳性的指数。
例如，如果球从10米高落下弹跳到6米高，这个索引就是0.6，并且球在一次弹跳之后的运动距离是16米。
如果球继续弹跳，两次弹跳后的距离将会是10米+6米+6米+3.6米=25.6米
注意: 每次后续的弹跳运动的距离，都是到地板距离加上这个距离的0.6倍，这个0.6倍就是球反弹回来的距离
编写一个程序，让用户输入球的一个初始以及允许球持续弹跳的次数。输出应该是球所运动的总距离
"""


def distance():
    init_heigh = input("please input the init heigh: ")
    total_count = input("please input the total count: ")
    init_heigh = float(init_heigh)
    total_count = int(total_count)
    sort_id = 0.6
    total_distance = 0

    for i in range(total_count):
        total_distance += init_heigh + init_heigh * sort_id
        init_heigh = init_heigh * sort_id


    print("The total distance is: ", total_distance)


if __name__ == '__main__':
    distance()

