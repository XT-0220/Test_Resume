# a="hello"和b="你好"编码成bytes类型


a = b"hello"
b = "你好".encode()
print(a, b)
print(type(a), type(b))
