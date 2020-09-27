# 格式：
# map(func, seq1[, seq2,…])
# 第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。
# Python函数编程中的map()函数是将func作用于seq中的每一个元素，并将所有的调用的结果作为一个list返回。如果func为None，作用同zip()。

list = [1,2,3,4,5]
def fn(x):
    return x ** 2
res = map(fn , list)
res = [i for i in res if i > 10]
print(res)




