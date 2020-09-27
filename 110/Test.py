# 一行代码实现1--100之和
a = sum(range(0,101))
print(a)

# 如何在一个函数内部修改全局变量
a = 1
def fn():
    global a
    a = 2
# 调用函数
fn()
print(a)

# 列出5个python标准库
# os re requests random pillow

# 字典如何删除键和合并两个字典
a = {'name':'xt', 'age':20}
del a['name']
print(a)
b = {'sex':'men'}
a.update(b)
print(a)

# 谈下python的GIL
# 全局解释器锁
# 多进程的情况下,每个进程都会被系统分配资源,相当于每个进程都有一个python解释器,所以多进程可以实现多个进程的同时运行

# python实现列表去重的方法
list = [1 , 1 , 2, 3, 8]
a = set(list)
print(a)

# python内建数据类型有哪些
# int str tuple  list dict

# 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
list = [1,2,3,4,5]
def fn(a):
    return a ** 2
res = map(fn,list)
res1 = [x for x in res if x > 10]
print(res1)

# python中生成随机整数、随机小数、0--1之间小数方法
import random
import numpy as np

q = np.random.randn(5)
w = random.random()
e = random.randint(0,3)
print(q)
print(w)
print(e)

# 数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
# select distint name from student

# 10个Linux常用命令
# ls cd cd . cd ~ cd .. pwd touch mkdir mv cp rm tree cat

# 列出python中可变数据类型和不可变数据类型，并简述原理
# 可变数据类型 list dict
# 不会创建一个对象 , 内存地址改变
# 不可变数据类型 str int tuple
# 新建了一个对象, 内存地址不会改变


# s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
# s1 = "ajldjlajfdljfddd"
# s1 = list(set(s1))
# s1.sort(reverse=False)
# res = "".join(s1)
# print(res)


# 用lambda函数实现两个数相乘
a = lambda x,y:x * y
print(a(1, 2/8))


# 字典根据键从小到大排序
dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

a = sorted(dict.items(),key=lambda i:i[0],reverse=False)
print(a)

# 利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
from collections import Counter

l = "kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"

a = Counter(l)
print(a)

# 字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三  深圳"
