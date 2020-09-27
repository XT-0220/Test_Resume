# s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']

import re

s="info:xiaoZhang 33 shandong"
a = re.split(r":| ",s)
print(a)