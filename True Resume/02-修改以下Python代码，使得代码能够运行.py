# 修改以下Python代码，使得代码能够运行



class A(object):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b

    def show(self):
        print("a=",self.__a,"b=",self.__b)

a = A(5,10)
a.show()
a(20)
