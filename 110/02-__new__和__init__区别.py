class bike:
    def __init__(self,newWheelNum,newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    def move(self):
        print("车会跑")

#创建对象
BM = bike(2, "green")

print("color:%s" % BM.color)
print("wheelNum:%s" % BM.wheelNum)


class A:
    def __init__(self):
        print("this is init methods", self)

    def __new__(cls, *args, **kwargs):
        print('this is cls ID', id(cls))
        print('this is new methods', object.__new__(cls))
        return object.__new__(cls)

A()
print('this is A ID',id(A))