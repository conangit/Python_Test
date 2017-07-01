#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import functools

# 255 = 0xff = O377 = 0b11111111
print(int('255'))
print(int('ff', 16))
print(int('377', base=8))
print(int('11111111', base=2))

def int2(x, base=2):
    return int(x, base)

print(int2('1111'))
print(int2('1001'))

int16 = functools.partial(int, base=16)
print(int16('ff'))
print(int16('10'))
print(int16('10', base=10))

def person(name, age, city):
    print('%s: %d, %s' %(name, age, city))

person('lihong', 20, 'Guangzhou')

person_gz = functools.partial(person, city = 'GZ')
person_gz('yaya', 24)

person_age = functools.partial(person, age = 30)
#person_age('lihong', 'SZ') ?

'''
总结：
当函数参数个数太多，需要简化时，使用functools.partial()可以创建一个新函数，
这个新函数可以固定原函数的部分参数，从而使调用更简单。
'''




