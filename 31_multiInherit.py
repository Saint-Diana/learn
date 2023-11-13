'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 21:51:30
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 22:34:37
FilePath: \learn\31_multiInherit.py
Description: python的多继承

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
class FatherA:
    def __init__(self, name) -> None:
        self.name = name
    
    def showA(self):
        print('父类A中的方法')
    
class FatherB:
    def __init__(self, age) -> None:
        self.age = age
    
    def showB(self):
        print('父类B中的方法')

class Son(FatherA, FatherB):
    def __init__(self, name, age, gender) -> None:
        # 调用父类的初始化方法
        FatherA.__init__(self, name)
        FatherB.__init__(self, age)
        self.gender = gender
    

son = Son('shc', 21, 'male')
son.showA()
son.showB()

# 如同c++中一样，也会存在菱形继承的问题