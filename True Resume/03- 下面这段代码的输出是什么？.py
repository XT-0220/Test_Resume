# 下面这段代码的输出是什么？

class B(object):
    def __init__(self):
        print("B init")

    def run(self):
        print("B run func")


class A(object):
    def run(self):
        print("A run func")

    def __new__(cls, a):
        print("new",a)
        if a>10:
            return super(A,cls).__new__(cls)
        return B()

    def __init__(self,a):
        print("init",a)


a1 = A(5)
a1.run()
a2 = A(20)



#------------------------------------------


num  = 9
def fn1():
    num = 20

def fn2():
    print(num)

fn2() # 9
fn1() # 啥都没有
fn2() # 9
