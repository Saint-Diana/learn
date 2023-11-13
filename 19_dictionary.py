'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-12 14:47:57
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-12 15:05:40
FilePath: \learn\19_dictionary.py
Description: 

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 字典 —— 其实就相当于Map
# 字典的键只能是不可变类型的数据 —— 例如基本数据类型、字符串、元组
# 字典的创建方法：
# 1、使用{}
d1 = {1: 10, 'str': 20, (3, 5): ['hello', 'world', 1]} # 如果key相同，那么value会进行覆盖

# 2、使用dict()和zip()
lst1 = [1, 2, 3, 4, 5, 6]
lst2 = ['cat', 'dog', 'pig', 'fish', 'horse']
d2 = dict(zip(lst1, lst2))

# 3、使用参数创建字典
t = (10, 20, 'hello')
d3 = dict(cat = 10, dog = 30)
d4 = {t: 20}

print(d1)
print(d2) # 如果key的数量不等于value的数量，映射产生的字典中k-v对数量以少的为准
print(d3)
print(d4)

# 通过提供key获取字典中的value
print(d1.get(10, '不存在')) # 使用get函数，如果字典中不存在我们提供的key，那么也不会报错，而是会返回None或者我们自定义的默认值
print(d1.get(1))

# 字典的遍历
for item in d1.items():
    print(item) # key=value组成的一个元组item

for key, value in d1.items(): # 也可以把元组拆开为key和value
    print(key, ':', value)