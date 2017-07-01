#!/usr/bin/env python3
# -*-coding: utf-8 -*-

from hello import Hello

h = Hello()
h.hello()
h.hello('lihong')

print(type(Hello))
print(type(h))

print('------')

def fn(self, name='world'):
    print('Hello, %s' % name)

Hong = type('Hong', (object,), dict(hong=fn))       #type()动态创建类
hh = Hong()
print(type(Hong))
print(type(hh))
hh.hong()
hh.hong('Hanmei')
