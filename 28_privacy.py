'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 21:15:16
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 21:27:27
FilePath: \learn\28_privacy.py
Description: python中的访问控制权限

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
# 1.self._xxx 这种实例属性是受保护的，只能本类和子类访问
# 2.self.__xxx 这种实例属性是私有的，只能本类进行访问
# 3.self.xxx 这种是普通的实例属性，类的内部、外部及子类都可以访问
# 同理，方法也分为这三类
class Student:
    def __init__(self, name, age, gender) -> None:
        self._name = name
        self.__age = age
        self.gender = gender
    
    def _fun1(self):
        print('子类及本类可以访问')

    def __fun2(self):
        print('只有本类可以访问')
    
    def show(self):
        # 类本身可以访问_fun1()和__fun2()
        self._fun1()
        self.__fun2()
        print(self._name)
        print(self.__age)

stu = Student('zy', 21, '男')
# 类的外部无法访问__age以及__fun2()
print(stu._name)
# print(stu.__age) # AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?
stu._fun1()
# stu.__fun2() # AttributeError: 'Student' object has no attribute '__fun2'. Did you mean: '_fun1'?

# 对于私有的实例和方法，需要按照obj._Class__attribute/function()的形式进行访问
print(stu._Student__age)
stu._Student__fun2()