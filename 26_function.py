'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 11:15:29
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 15:32:23
FilePath: \learn\26_function.py
Description: python函数

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# def sum(a: int, b: int) -> int:
#     if(type(a) != int or type(b) != int):
#         raise TypeError('类型错误')
#     return (a + b)

# a = 10
# b = 2
# print(sum(a, b))


def happyBirthday(name, age):
    print('祝', name, age, '岁生日快乐')

happyBirthday('shc', 21)

happyBirthday('shc', age=21)

# happyBirthday(name='shc', 18) # 语法错误


# 带默认值的函数
def funcWithDefaultArgs(name='shc', age=21):
    print(name, '今年', age, '岁')

funcWithDefaultArgs(20) # 默认值默认从前开始赋值，不会说前面的参数使用默认值，后面的参数反而用用户提供的参数

funcWithDefaultArgs('周扬')

# 可变参数
# 又分为个数可变的位置参数(*param) 和 个数可变的关键字参数(**param)

# 1.个数可变的位置参数，会把提供的若干个参数放到元组当中
def fun(*param):
    print(type(param))
    for item in param:
        print(item)

# 可以传递若干个值(0个~无限个)
fun()
fun(20)
fun(20, 30, 40)
fun(20, 30, 40, 50)
fun([1, 2, 3, 4]) # 实际上传递的是1个参数
# 在调用时，参数前加一颗*，会把列表解包
fun(*[1, 2, 3, 4]) # 实际传递的是4个参数


# 2.个数可变的关键字参数
def fun2(**param):
    # 这里的param是一个dict，包括key和value
    print(type(param))
    for key, value in param.items():
        print(key, '->', value)

fun2(name='shc', age=18, height=172)


# 多个返回值的函数 —— 会把多个返回值封装为元组进行返回
def calc(a, b):
    return (a + b), (a - b), (a * b), (a / b)

result = calc(3, 5)
print(type(result))
print(result)

# lambda 或者说是箭头函数
# sum = lambda a, b: a + b;
# print(sum(1, 3))

def power(n):
    if(n == 0):
        return 1
    return n * power(n - 1)

print(power(10))

# range()产生的不是列表
print(type(range(1, 11)))
lst = list(range(1, 11))
tp = tuple(range(1, 11))
st = set(range(1, 11))
print(lst)
print(tp)
print(st)
print(sum(lst))