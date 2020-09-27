# 列表嵌套元组，分别按字母和数字排序

# 根据元组中的切片来分别对字母和数字进行排序
foo = [('xt', 20), ('yj', 2), ('aa', 11), ('bb', 15)]
a = sorted(foo, key=lambda x: x[1], reverse=False)
print(a)
b = sorted(foo, key=lambda y:y[0])
print(b)


# 列表嵌套列表排序，年龄数字相同怎么办？
foo = [('xt', 20), ('yj', 20), ('aa', 11), ('bb', 15)]
a = sorted(foo, key=lambda x: (x[1], x[0]))
print(a)

b = sorted(foo, key=lambda y: y[0])
print(b)