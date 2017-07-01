#!/usr/bin/env python3
# -*-coding: utf-8 -*-

class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = Student()
s.set_score(90)
print(s.get_score())


class Std(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s1 = Std()
s1.score = 70
print(s1.score)

s2 = Std()
#s2.score = 'kk'
#s2.score = -3


class Person(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):       #可对参数进行检测
        self._birth = value

    @property
    def age(self):
        return 2017 - self._birth

p1 = Person()
p1.birth = 1991
print(p1.birth)
print(p1.age)
#p1.age = 34

'''
总结：
@property常用在类的定义中
@property把一个getter方法变成的属性
@property创建的另一个装饰器把setter方法变成属性赋值
@property可控制属性的可读可写性
'''

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        if not isinstance(value, (int, float)):
            raise ValueError('score must be an integer or float!')
        self._width = value

    @property
    def heigth(self):
        return self._heigth

    @heigth.setter
    def heigth(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('score must be an integer or float!')
        self._heigth = value

    @property
    def resolution(self):
        return self._width * self._heigth

res = Screen()
res.width = 100.4
res.heigth = 45.5
print(res.resolution)
