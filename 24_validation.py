'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 10:16:03
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 10:35:16
FilePath: \learn\24_validation.py
Description: 字符串的校验方法

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
s = '123'
print(s.isdigit()) # 所有字符都是数字(阿拉伯数字)

print(s.isnumeric()) # 所有字符都是数字(可以识别中文数字、罗马数字等)

print(s.isalpha()) # 所有字符都是字母(包含中文字符) alphabet

print(s.isalnum()) # 所有字符都是数字或字母(包含中文字符)

print(s.islower()) # 所有字符都是小写

print(s.isupper()) # 所有字符都是大写

print(s.istitle()) # 所有字符都是首字母大写

print(s.isspace()) # 所有字符都是空白字符(\n, \t等)

print('一二三'.isnumeric()) # 可以识别出来
print('壹贰叁'.isnumeric()) # 可以识别出来
print('ⅠⅡⅢ'.isnumeric()) # 可以识别出来


# 字符串的去重操作
s = 'hhhdsadasdshdahsdhasdxjsaxkjasjkwuq'

# (1)字符串拼接及not in
newS = ''
for item in s:
    if(item not in newS):
        newS += item

print(newS)

# (2)使用索引加not in
newS = ''
for i in range(len(s)):
    if(s[i] not in newS):
        newS += s[i]

print(newS)


# (3)通过集合去重加列表排序
# 首先把字符串变成集合
newS = set(s)
lst = list(newS)
lst.sort(key=s.index)
print(''.join(lst))