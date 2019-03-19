# _*_ codfing: utf-8 _*_
__author__ = 'zhangedison'

"""
编写一个程序，它以球体的半径(浮点数)作为输入，并且输出球体的直径、圆周长、表面积和体积
球体体积：4/3*圆周率*半径的立方
球的表面积：4*圆周率*半径的平方
圆周率一般取3.14
周长的公式是：c＝πd或c＝2πr

半径  radius

直径   diameter

圆周长   circumference

圆体积   Round volume

圆面积   Round area

"""


def circle_calculation():
    pi = 3.14
    radius = input("please input radius: ")
    radius = float(radius)
    if radius <= 0:
        print("The radius must greater than 1")
    else:
        diameter = 2 * radius
        circumference = 2 * pi * radius
        round_volume = 4/3 * pi * pow(radius, 3)
        round_area = 4 * pi * pow(radius, 2)
        print("The radius is:", round(radius,2))
        print("The diameter is:", round(diameter, 2))
        print("The circumference is:", round(circumference, 2))
        print("The round volume is:", round(round_volume, 2))
        print("The round area is:", round(round_area, 2))

if __name__ == '__main__':
    circle_calculation()