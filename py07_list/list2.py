#!/usr/bin/env python3
# -*- coding: utf-8 -*-

lst = ['name', 40, 90.5, True]
print('lst:')
print('%s' %(lst[0]))
print('%d' %(lst[1]))
print('%f' %(lst[2]))
print(lst[3])

lst2 = ['new list', lst,]
num1 = len(lst)
num2 = len(lst2)
print('lst len:%d' %num1)
print('lst2 len:%d' %num2)
print('%s' %(lst2[1][0]))
print('%s' %(lst2[1][3]))







