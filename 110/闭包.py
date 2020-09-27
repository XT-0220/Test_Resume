def check(fn):
    def innner():
        print("login..")
        fn()

    return innner

@check  # 语法糖
def comment():
    print("comment..")

# comment =check(comment)
comment()



# 闭包
def func_outter(a):
    def func_inner(b):
        re = a + b
        print(re)
    return func_inner

f = func_outter(1)

f(2)
