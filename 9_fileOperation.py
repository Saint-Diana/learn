'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-10 21:47:36
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-10 22:12:57
FilePath: \learn\2-9_fileOperation.py
Description: 使用python的文件操作，从./test/input.txt中读取内容，然后写入到./test/output.txt中

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
file_input = open('./test/input.txt', 'r', encoding='utf-8') # 需要指定使用'utf-8'编码打开文件
print('打开的文件名：' + file_input.name)
print('是否已关闭：', file_input.closed, sep='')
print('访问模式：' + file_input.mode)
content = file_input.read() # 读取文件的全部内容
file_input.close()

file_output = open('./test/output.txt', 'w', encoding='utf-8')
file_output.write(content)
file_output.close()


# 如果想要逐行读/写，就需要使用到循环和readline()函数
with open('./test/input.txt', mode='+r', encoding='utf-8') as input_file:
    # 使用for循环逐行读取文件
    for line in input_file:
        # 打印每一行的内容
        print(line, end='')

# 也可以直接使用print('xxx', file=xxx)来直接写入文件
file_output = open('./test/output.txt', '+w', encoding='utf-8')
print('使用print进行写入', file=file_output)