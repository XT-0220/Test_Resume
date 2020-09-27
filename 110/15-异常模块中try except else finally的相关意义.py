# 举例说明异常模块中try except else finally的相关意义

try:
    num = 100
    print(num)
except NameError as errorMsg:
    print("error:%s" % errorMsg)
else:
    print("没有捕获到异常 , 则执行该语句")


try:
    num = 100
    print(num)
except NameError as errorMsg:
    print("error:%s" % errorMsg)
finally:
    print("不管是否捕获到异常，都执行该语句")