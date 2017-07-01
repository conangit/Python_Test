#!/usr/bin/env python3
#-*-coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')
a = Animal()
d = Dog()
d.run()    #覆盖父类的方法
c = Cat()
c.run()

print(isinstance(d, Animal))    #子类是特殊的父类
print(isinstance(c, Animal))
print(isinstance(a, Animal))
print(isinstance(a, Dog))

def run2(animal):
    animal.run()

run2(a)
run2(d)
run2(c)

#鸭子类型
class SB(object):
    def run(self):
        print('SB is runing...,haha!!')

sb = SB()
run2(sb)
print(isinstance(sb, SB))
print(isinstance(sb, Animal))

print(type(a))
print(type(d))
print(type(c))
print(type(sb))

print(isinstance(d, Animal))        # True
print(type(d) == type(a))           # False

print(dir(c))       # c--Cat实例的属性和方法

print(dir('abc'))

