#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add_end(L=[]):
	L.append('end')
	return L

print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

print(add_end())
print(add_end())
print(add_end())

def add_end_2(L=None):
	if L is None:
		L = []
	L.append('end')
	return L

print(add_end_2([1, 2, 3]))
print(add_end_2(['x', 'y', 'z']))

print(add_end_2())
print(add_end_2())
print(add_end_2())

	