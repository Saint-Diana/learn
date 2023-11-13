'''
Author: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
Date: 2023-11-13 16:18:36
LastEditors: Huichang Shen 85936940+Saint-Diana@users.noreply.github.com
LastEditTime: 2023-11-13 17:43:49
FilePath: \learn\27_class.py
Description: 学习python中如何创建类

Copyright (c) 2023 by Huichang Shen 85936940+Saint-Diana@users.noreply.github.com, All Rights Reserved. 
'''
class Student:
    # 类属性：定义在类中，方法外的变量 —— 类似于static修饰的属性
    # 类属性是在类中定义的属性，它是和这个类所绑定的，这个类中的所有对象都可以访问。访问时可以通过类名来访问，也可以通过实例名来访问
    school = '武汉理工大学'
    # 实例属性：定义在初始化方法__init__中，使用self.xxx来定义 —— 类似于java中的私有属性
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show(self) -> None:
        # 必须使用self.xxx调用实例属性
        print('我叫', self.name, '，今年', self.age, '岁了')
    
    # 静态方法 —— 不能调用实例属性，也不能调用实例方法
    @staticmethod
    def display() -> None:
        print('静态方法不能调用实例属性，也不能调用实例方法')

    @classmethod
    def cm(cls) -> None: # cls 是 class 的缩写
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')

student = Student('shc', 21)
student.show()

student2 = Student('zy', 21)

# 类属性是所有对象共享的， 使用类名进行调用
Student.school = 'whut'

print(student.school)
print(student2.school)

# 为对象动态绑定一个实例属性
student.height = 172.3
print(student.height)

# 其他对象不会有
# print(student2.height) # AttributeError: 'Student' object has no attribute 'height'

# 为对象动态绑定方法
student.hello = lambda : print('hello')
student.hello()

# 其他对象不会有
# student2.hello() # AttributeError: 'Student' object has no attribute 'hello'