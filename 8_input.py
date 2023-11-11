'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-10 21:27:17
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-10 21:44:50
FilePath: \learn\2-8_input.py
Description: input()函数默认将输入的内容作为字符串，如果想要作为其他数据类型，需要先手动进行转换

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
name = input('请输入您的姓名：')
print('姓名为' + name)

num = input('请输入您的幸运数字：')
num = int(num) # 转换为int类型
print('幸运数字是', num)

a = 10
b = 20
c = 30
print(a, b, c, sep=',', end='', file=None) # sep设置分隔符、end设置结束符、file设置是否输出到文件