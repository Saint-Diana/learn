'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 10:37:46
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 11:13:44
FilePath: \learn\25_exception.py
Description: 异常处理 相较于java中的try ··· catch ··· finally ···，python中使用try ··· except ··· else ··· finally ···来进行

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 如果num2输入为0，那么就会报错ZeroDivisionError: division by zero
try:
    num1 = eval(input('请输入一个整数：'))
    num2 = eval(input('请输入另一个整数：'))
    result = num1 / num2
    print('结果为{0:.2f}'.format(result))
except NameError:
    print('输入错误')
except ZeroDivisionError:
    print('除数为零，请重新输入')
except BaseException:
    print('未知异常')
else: # 没有异常要执行的代码
    print('没有异常，程序正常执行')
finally: # 不论有没有异常都会执行的代码
    print('不论有没有异常,一定会执行')