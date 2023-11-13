'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 21:27:39
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 21:35:06
FilePath: \learn\29_@property.py
Description: 使用@property来修饰方法，使其变为属性的形式，调用可以去掉括号

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
class Student:
    def __init__(self, name, gender) -> None:
        self.name = name
        self.__gender = gender # self.__gender 是私有的实例属性
    
    # 本质上是私有属性的getter
    # 使用@property 修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender
    
    # 为私有属性设置setter
    @gender.setter
    def gender(self, gender):
        self.__gender = gender

stu = Student('zy', 'male')
print(stu.name, stu.gender)
stu.gender = 'female' # 虽然这里看起来好像是在给属性赋值，实际上是在调用方法gender()
# 这样就可以实现在外部访问私有实例属性
print(stu.name, stu.gender)