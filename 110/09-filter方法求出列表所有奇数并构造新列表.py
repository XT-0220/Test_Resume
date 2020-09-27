# filter方法求出列表所有奇数并构造新列表，a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def fn(a):
    return a %2 == 1
new_list = filter(fn , a)
new_list = [i for i in new_list]
print(new_list)