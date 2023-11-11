'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-11 11:30:10
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-11 12:21:10
FilePath: \learn\10_dataType.py
Description: 了解python中的数据类型

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 数值类型

# 浮点数(float)
# a = 0.1
# b = 2e-1
# print('a的数据类型为', type(a))
# print('b的数据类型为', type(b))
# c = a + b
# print('c的数据类型为', type(c), 'c的值为', c)
# d = 0.1 + 0.3
# print('d的数据类型为', type(d), 'd的值为', d)

# 复数(complex)
# x = 1 + 3j
# y = -5 + 6j
# print('x的数据类型为', type(x))
# print('y的数据类型为', type(y))
# print('x + y的数据类型为', type(x + y), 'x + y的值为', x + y)

# 字符串
city = '湖北省武汉市'
address = '武汉理工大学南湖校区'
print(city + address, end='')
multiLines = '''
    abc
    def
    ghi
'''
print(multiLines, end='')

# 转义字符
print('北京\n欢迎你') # \n是转义字符，换行
print(r'北京\n欢迎你') # 使用r/R放在字符串前，使得所有转义字符都失效

s = 'hello world'
print(s[0], type(s[0])) # python当中没有字符型，所有的都看成是字符串
print(s[-3]) # 负的下标就是倒着数(从-1开始)
print(s[2:6])
print(s[:5])
print(s[3:])
print(s[-6:-3])

# 字符串操作：+、*、in
str1 = 'hello'
str2 = 'world'
print(str1 + str2) # +用于字符串连接
print(str1 * 3) # x*n，复制n次字符串x
if ('he' in str1): # x in s，如果x是s的子串，结果为True，否则结果为False
    print('str1包含he')
else:
    print('str1不包含he')

print('hello world'[3])
m = chr(97) # chr()只能用于代码和字符的转换
print(m)
print(ord(m)) # ord()用于把字符转换为对应的代码
print(ord('滚')) # ord()用于把字符转换为对应的代码
