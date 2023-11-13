'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 10:04:53
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 10:15:50
FilePath: \learn\23_encode&decode.py
Description: 字符串的编码和解码

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 编码和解码必须使用相同的字符集，否则会产生乱码！
# 字符串的编码就是把str类型转换成bytes类型，需要用到字符串的encode()方法
s = '你好 世界'
bs = s.encode(encoding='utf-8')
print(bs)

# 字符串的解码就是把bytes类型转换成str类型，需要用到bytes类型的decode()方法
s = bs.decode(encoding='utf-8') # 如果使用其他字符集，会解码产生乱码
print(s)