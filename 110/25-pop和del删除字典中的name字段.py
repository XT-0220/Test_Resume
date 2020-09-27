# 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}


dic={"name":"zs","age":18}

del dic["name"]
print(dic)

dic.pop("name")
print(dic)