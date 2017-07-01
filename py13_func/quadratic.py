#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
	dd = b*b - 4*a*c
	if dd < 0:
		raise TypeError('illegal parameter')
	else:
		x1 = (-b + math.sqrt(dd)) / (2*a)
		x2 = (-b - math.sqrt(dd)) / (2*a)
	return x1, x2

print(quadratic(1, 4, 4))
print(quadratic(1, -4, 4))
print(quadratic(1, 6, 6))
print(quadratic(1, 2, 4))
		
