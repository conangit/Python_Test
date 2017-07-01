#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['lihong', 'linxianfeng', 'ok']
print('%s' %(classmates))

mun = len(classmates)
print('num: %d' %(mun))

print('%s' %(classmates[0]))
print('%s' %(classmates[1]))
print('%s' %(classmates[2]))
#print('%s' %(classmates[3]))

print('%s' %(classmates[-1]))
print('%s' %(classmates[-2]))
print('%s' %(classmates[-3]))

classmates.append('last')
print('%s' %(classmates))

classmates.insert(1, 'second')
print('%s' %(classmates))

classmates.pop(1)
print('%s' %(classmates))

classmates[0] = 'first'
print('%s' %(classmates))



