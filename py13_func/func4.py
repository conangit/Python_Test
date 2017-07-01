#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x, n):
	s = 1
	while n > 0:
		n = n-1
		s = s * x
	return s

print(power(2, 3))
print(power(4, 2))

def power2(x, n=3):
	s = 1
	while n > 0:
		n = n-1
		s = s * x
	return s

print(power2(3))
print(power2(4))
