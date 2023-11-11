'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-11 15:54:00
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-11 16:03:16
FilePath: \learn\14_choiceStruct.py
Description: python中使用elif替代'else if'

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 选择结构
number = eval(input('请输入您的六位中奖号码：'))
if(number == 987654):
    print('一等奖')
elif(number == 654321):
    print('二等奖')
else:
    print('三等奖')

# 嵌套if
a, b, c = 10, 5, 15
if(a >= b):
    if(b >= c or a >= c):
        print('a最大')
    else:
        print('c最大')
else:
    if(b >= c):
        print('b最大')
    else:
        print('c最大')

# python3.11新特性——模式匹配
score = input('请输入成绩的等级：')
match score:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('中等')
    case 'D':
        print('及格')
    case 'E':
        print('不及格')