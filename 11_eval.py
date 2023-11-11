'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-11 15:22:14
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-11 15:24:46
FilePath: \learn\11_eval.py
Description: eval函数的使用

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
s = '3.14+3'
print(s, type(s))
x = eval(s) # 使用eval函数去掉s这个字符串左右的引号，会根据字符串的内容进行计算，得出结果
print(x, type(x))

# eval函数通常与input函数一同使用，用于获取用户输入的数据
age = eval(input('请输入您的年龄：'))
print('年龄为', age, '类型为', type(age))

# 但是如果使用print(eval('hello'))就会报错，因为相当于运行print(hello) -> hello会被当成变量