#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_abs(x):
	if not isinstance(x, (int, float)):
	    raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(10))
print(my_abs(-5))

print(my_abs('a'))
#print(abs('a'))


