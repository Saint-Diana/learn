'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-12 15:12:32
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-12 15:25:27
FilePath: \learn\20_set.py
Description: 

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 集合 —— 集合当中只能存储不可变数据类型、集合中不存在重复元素、集合元素顺序随机
s = {10, 20, (1, 2), 'hello', 'hello', 'hello'} # 会自动删除相同元素，只保留一个
print(s)

# s.add([1, 2, 3]) # 会报错 TypeError: unhashable type: 'list'

s = set('helloworld')
print(s)

# 集合之间的操作
A = {10, 20, 30, 40}
B = {20, 30, 50}

# 求交集
print('-' * 40)
print(A & B)

# 求并集
print('-' * 40)
print(A | B)

# 求差集
print('-' * 40)
print(A - B) # A - B = A - (A & B)
print(A - (A & B))

# 求补集
print('-' * 40)
print(A ^ B) # A ^ B = (A | B) - (A & B)
print((A | B) - (A & B))