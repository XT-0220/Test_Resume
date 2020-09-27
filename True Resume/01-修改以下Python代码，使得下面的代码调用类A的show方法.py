# 修改以下Python代码，使得下面的代码调用类A的show方法?


class A(object):
    def run(self):
        print("基础 run 方法")

class B(A):
    def run(self):
        print("衍生 run 方法 ")


obj = B()
obj.run()
