'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 21:37:29
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 21:45:09
FilePath: \learn\30_inherit.py
Description: python的继承机制，类似于c++，是多继承

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
class Human:
    def __init__(self, name, age, gender) -> None:
        self.__name = name
        self.__age = age
        self.__gender = gender
    
    # 生成setter和getter
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age
    
    @property
    def gender(self):
        return self.__gender
    
    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    # 公有方法
    def display(self) -> None:
        print(self.__name, '，性别', self.__gender, '，今年', self.__age, '岁')

# 子类S
class Student(Human):
    def __init__(self, name, age, gender, school) -> None:
        # 子类要先使用super()来调用父类的初始化方法
        super().__init__(name, age, gender)
        self.__school = school
    
    # 新增的属性
    @property
    def school(self):
        return self.__school
    
    @school.setter
    def school(self, school):
        self.__school = school
    
    # 重写display()方法
    def display(self) -> None:
        return super().display()