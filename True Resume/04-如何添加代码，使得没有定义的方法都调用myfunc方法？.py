# 如何添加代码，使得没有定义的方法都调用myfunc方法？

class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print("初始化方法")

    def myfunc(self):
        print("myfunc")


a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()
