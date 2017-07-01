#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc(num):
	sum = 0
	for n in num:
		sum += n * n
	return sum

print([1, 2])
print(calc([1, 2]))

print([1, 2, 3])
print(calc([1, 2, 3]))

def calc_2(*num):
	sum = 0
	for n in num:
		sum += n * n
	return sum

print(calc_2(1, 2, 3))
print(calc_2(1, 2, 3, 4))

ll = [1, 3, 5]
print(calc_2(ll[0], ll[1], ll[2]))
print(calc_2(*ll))

	