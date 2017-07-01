#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#关键字参数
def person(name, age, **kw):
	print('person: ', name, age, 'other:', kw)

person('lihong', 20)

person('lihong', 20, city='guanghou')
#person('lihong', 20, 'guanghou')	#'guanghou'解析为位置参数，而不是关键字参数

person('lihong', 20, make='num')

person('lihong', 20, num=50)
#person('lihong', 20, 50='num')
#person('lihong', 20, 20=50)
#person('lihong', 20, '20'=50)
#person('lihong', 20, str(20)=50)

extra = {'city':'Beijing', 'job':'Engineer'}
person('lihong', 20, **extra)

#命名关键字参数
def pr(name, age, *, city, job):
	print('per: ', name, age, city, job)

pr('lihong', 20, city='guanghou', job='chaocai')
#pr('lihong', 20, city='guanghou')	#miss keyword
#pr('lihong', 20, city='guanghou', job='chaocai', hobby='happy')	#unexpected keyword


def pr_2(name, age, *arg, city, job):
	print('per_2: ', name, age, city, job, *arg)


pr_2('lihong', 20, city='guanghou', job='chaocai')
#pr_2('lihong', 20, 'guanghou', 'chaocai')  #必须传入参数名
#pr_2('lihong', 20, 'guanghou', 'chaocai')
pr_2('lihong', 20, 78, city='guanghou', job='dajiangyou')
#pr_2('lihong', 20, city='guanghou', job='dajiangyou', 78)



def func1(a, b, c=0, *arg, **kw):
	print('func1: ', a, b, c, arg, kw)

func1(1, 2)
func1(1, 2, 3)
func1(1, 2, 3, 4)
func1(1, 2, 3, 4, 5)
func1(1, 2, 3, 4, 5, name='lihong')

def f2(a, b, c=0, *, name):
	print('f2: ', a, b, c, name)
	
f2(1, 2, name='lihong')

"""
def f3(a, b, c=0, *arg, *, name):
	print('f3: ', a, b, c, arg, name)

f3(1, 2, 5, 'ok', name='lihong')
"""

def f4(a, b,c=0, *, d, **kw):
	print('f4: ', a, b, c, d, kw)

f4(1, 2, 3, d=99, name='lihong')

"""
def f5(a, b, c=0, *arg, *, name):
	print('f5: ', a, b, c, arg, name)

f5(1, 2, 5, 'ok', name='lihong')
"""
