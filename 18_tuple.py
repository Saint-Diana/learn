'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-12 14:29:52
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-12 14:49:45
FilePath: \learn\18_tuple.py
Description: 

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 元组 —— python内置的不可变序列
# 元组也有两种创建方式
# 1、即便只有一个元素，也不可以省略逗号
t1 = (1, )

# 2、使用tuple()进行创建
t2 = tuple(['hello', 'world', 1, 2, 3, 10, 20, 50, 100])
t3 = tuple('helloWorld')

print(t1)
print(t2)
print(t3)

print('10在元组t2中存在：', (10 in t2))
print('10在元组t2中不存在：', (10 not in t2))
print('元组t3中的最小值：', min(t3))
print('元组t3中的最大值：', max(t3))
print('元组t1的长度：', len(t1))
print('元组t3中l的个数：', t3.count('l'))
print('元组t2中3的下标：', t2.index(3))

# 删除元组
del t1, t2, t3