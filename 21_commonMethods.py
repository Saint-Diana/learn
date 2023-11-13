'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 09:33:01
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 09:49:31
FilePath: \learn\21_commonMethods.py
Description: 字符串常用方法

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 大小写转换
s = 'heLlO wOrld'
newS = s.upper()
print(newS)
newS = s.lower()
print(newS)


# 字符串的分割
lst = s.split(' ')
print(lst)

# 检索操作
pos = s.find('O') # 查找'O'在字符串s中首次出现的位置
print(pos)

pos = s.find('o') # 没有找到，返回-1
print(pos)

# 前缀和后缀
print('demo.java'.endswith('java'))
print('text.txt'.startswith('text'))

# 字符串替换
newS = s.replace('O', '$', 1) # 默认全部替换，可以设置只替换一次
print(newS)

# 字符串居中
newS = s.center(20, '*')
print(newS)

# 去除左右空格
s = '   hello   world   '
print(s.strip()) # 去掉左右空格

print(s.lstrip()) # 去掉左侧空格

print(s.rstrip()) # 去掉右侧空格


# 可以类似于c语言当中的printf使用占位符进行输出
name = 'shc'
age = 21
height = 171.4
print('姓名为%s，年龄为%d，身高为%.1f' % (name, age, height))

# f-string
print(f'姓名:{name}, 年龄:{age}, 身高:{height}')

# 使用字符串的format方法
print('姓名:{0}, 年龄:{1}, 身高:{2}'.format(name, age, height))