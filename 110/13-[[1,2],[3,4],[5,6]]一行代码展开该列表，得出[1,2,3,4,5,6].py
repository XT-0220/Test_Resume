# [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
import numpy as np

a = [[1,2],[3,4],[5,6]]

# x = [j for i in a for j in i]
# print(x)

# for x in a:
#     print(x)
#     for y in x:
#         print(y)

# 将列表转成numpy矩阵，通过numpy的flatten（）方法
x = np.array(a).flatten().tolist()
print(x)