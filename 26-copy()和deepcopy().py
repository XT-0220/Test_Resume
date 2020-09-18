import copy

a = '你好'
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
print(a, id(a))
print(b, id(b))
print(c, id(c))
print(d, id(d))