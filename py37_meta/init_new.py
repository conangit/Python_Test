#!/usr/bin/env python2
# -*-coding: utf-8 -*-

'''
注意运行环境
'''

class Student(object):
    def __new__(cls, name, age):
        print('__new__ be called.')
        return super(Student, cls).__new__(cls, name, age)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('__init__ be called.')

    def __str__(self):
        return '<Object: %s(%s)>' % (self.name, self.age)

if __name__ == '__main__':
    s = Student('lihong', 70)
    print(s)


class PositiveInteger_1(int):
    def __init__(self, value):
        super(PositiveInteger_1, self).__init__(self, abs(value))

i = PositiveInteger_1(-3)
print(i)

class PositiveInteger_2(int):
    def __new__(cls, value):
        return super(PositiveInteger_2, cls).__new__(cls, abs(value))

ii = PositiveInteger_2(-3)
print(ii)

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

obj1 = Singleton()
obj2 = Singleton()

obj1.attr1 = 'value'
print(obj1.attr1)
print(obj2.attr1)
print(obj1 is obj2)



