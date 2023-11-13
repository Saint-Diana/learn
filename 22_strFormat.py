'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 09:51:45
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 10:01:40
FilePath: \learn\22_strFormat.py
Description: 使用字符串的format()进行格式控制

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
s = 'helloWorld'
print('{0:*<20}'.format(s)) # 字符串的显示宽度为20，左对齐，空白部分使用*填充
print('{0:$>20}'.format(s)) # 字符串的显示宽度为20，右对齐，空白部分使用$填充
print('{0:#^20}'.format(s)) # 字符串的显示宽度为20，居中对齐，空白部分使用$填充


# 浮点数
a = 13212323.4163131
print('{0:,}'.format(a)) # 给浮点数/整数添加上','分隔

print('{0:.2f}'.format(a)) # 保留两位小数

# 整数
a = 4113131
print('二进制{0:b}'.format(a)) # 二进制 :b
print('八进制{0:o}'.format(a)) # 八进制 :o
print('十进制{0:d}'.format(a)) # 十进制 :d
print('十六进制{0:X}'.format(a)) # 十六进制 :x/:X