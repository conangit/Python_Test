#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f1(n):
	if(n > 1):
		return n * f1(n-1)		#调用本身，但包含表达式
	else:
		return 1

print(f1(5))
#print(f1(100))
#print(f1(1000))

#尾归法
def fact(n):
	return fact_iter(n, 1)
	
def fact_iter(num, product):
	if 1 == num:
		return product
	return fact_iter(num-1, num*product)  #调用本身，不含表达式

print(fact(5))
#print(fact(1000))

#汉诺塔
def move(n, x, y, z):
	if n== 1:
		print('move', x, '-->', z)
	else:
		move(n-1, x, z, y)
		move(1, x, y, z)
		move(n-1, y, x, z)
	
move(3, 'A', 'B', 'C')

print('############')

def ff(n, x, y, z):
	if n== 1:
		print('move', x, '-->', z)
		return
	move(n-1, x, z, y)
	print('move', x, '-->', z)	
	move(n-1, y, x, z)
	
ff(3, 'A', 'B', 'C')




