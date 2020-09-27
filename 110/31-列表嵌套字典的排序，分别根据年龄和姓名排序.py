# 列表嵌套字典的排序，分别根据年龄和姓名排序
# foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]

foo = [{"name":"zs","age":19},{"name":"ll","age":54},{"name":"wa","age":17},{"name":"df","age":23}]

a = sorted(foo, key=lambda x: x["age"], reverse=False)
b = sorted(foo, key=lambda y: y["name"])

print(a)
print(b)