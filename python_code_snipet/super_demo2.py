# _*_ coding: utf-8 _*_

#单继承
class A:
    def __init__(self):
        self.n = 2
        print(self.n)

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n -= m
        print(self.n)


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print(self.n)
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3

if __name__ == '__main__':
    b = B()
    b.add(2)
    print(b.n)