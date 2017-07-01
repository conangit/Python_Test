#!/usr/bin/env python3
#-*-coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' %(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

s1 = Student('lihong', 70)
s2 = Student('mini', 95)

s1.print_score()
s2.print_score()
print(s1.get_grade())
print(s2.get_grade())

class Std(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set(self, name, age):
        self.__name = name
        self.__age = age
    def p(self):
        print('%s: %s' %(self.__name, self.__age))

s = Std('lihong', 20)
s.p()
print(s.get_name())
print(s.get_age())
s.set('yaya', 18)
s.p()

####
s.__name = 'hanmei'
s._Std__name = 'liyong'
s.p()
###