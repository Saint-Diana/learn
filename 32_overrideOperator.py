'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 22:38:49
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 22:44:20
FilePath: \learn\32_overrideOperator.py
Description: 通过重载__add__()等方法，可以重载运算符

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
class Complex:
    def __init__(self, real, imagine) -> None:
        self.real = real
        self.imagine = imagine
    
    def __add__(self, b):
        return Complex(self.real + b.real, self.imagine + b.imagine)

com1 = Complex(1, 2)
com2 = Complex(3, 4)
com3 = com1 + com2
print(com3.real, com3.imagine)