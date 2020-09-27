# list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]

# 从列表中依次取出最小值并删除 , 通过append添加到新列表


list=[2,3,5,4,9,6]
new_list = []
def get_min(list):
    a = min(list)
    list.remove(a)
    new_list.append(a)

    if len(list)>0:
        get_min(list)
    return new_list
res = get_min(list)
print(res)