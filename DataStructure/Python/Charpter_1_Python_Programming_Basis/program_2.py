# _*_ codfing: utf-8 _*_
__author__ = 'zhangedison'

"""
一个雇员一周的总薪水，等于其每小时的薪水乘以一周正常工作的小时数，再加上加班费。加班费等于总的加班时间乘以每小时薪水的1.5倍。
编写一个程序，以每小时的薪水、总的常规工作时间和总的加班时间作为参数，并且显示一个雇员的总周薪

时薪    hourly hour
加班    overtime
加班费  overtime pay
"""


def salary():
    hourly_hour = input("please input the hourly hour: ")
    work_hour = input("please input the work hour: ")
    over_time = input("please input the over time: ")

    hourly_hour = float(hourly_hour)
    work_hour = float(work_hour)
    over_time = float(over_time)
    overtime_pay = 1.5 * hourly_hour
    total_salary = hourly_hour * work_hour + overtime_pay * over_time
    print("This week, the salary is: ",round(total_salary, 2))

if __name__ == '__main__':
    salary()

