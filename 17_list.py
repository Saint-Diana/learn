'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-11 22:08:11
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-12 14:25:38
FilePath: \learn\17_list.py
Description: 

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 列表，元素可以是任意数据类型
# 创建的两种方式：
# 1.使用[]
import random


myList1 = [1, 10, 'a', 'd', [2, 4, 5]]

# 2.使用list()
myList2 = list()
myList2.append(1)
myList2.append(2)
myList2.append(3)
myList2.append(5)
myList2.append([10, 20, 30])

print(myList1)
print(myList2)


# 列表操作
# 在列表末尾添加一个1
myList1.append(1)
print(myList1)
# 会从头开始找，删除第一个1
myList1.remove(1)
print(myList1)
# 统计列表中'a'出现的次数
print(myList1.count('a'))


# 遍历列表
print(type(enumerate(myList1)))
for index, item in enumerate(myList1):
    print(index, item)

# 列表生成式
lst = [2 * item + 1 for item in range(0, 11)]
print(lst, id(lst))

lst1 = [2 * i for i in range(0, 11) if i < 5]
print(lst1, id(lst1))

# 生成包含10个随机数的列表
lst2 = [random.randint(1, 100) for _ in range(10)]
print(lst2)

print('-' * 30)
for i in range(len(lst2)):
    print(lst2[i])