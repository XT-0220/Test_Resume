# 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,5,6,7,8,9]

a = [1,5,7,9]
b = [2,2,6,8]

# c = list(a + b)
# c.sort(reverse=False)
# print(c)

a.extend(b)
print(a)
a.sort(reverse=False)
print(a)