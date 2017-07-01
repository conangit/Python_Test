#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#机制：边循环边计算

l = [i * i for i in range(5)]
print(l)

g = (i * i for i in range(5))
print(g)

'''
print(next(g))
print(next(g))
print(next(g))
'''

for n in g:
    print(n)
    

def fib1(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        print(b)
        a = b
        b = a + b    #实际b = b + b
        n = n + 1
    return 'done'

    
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b, n = b, a+b, n+1
    return 'done'

print(fib1(7))    
print(fib2(7))

def fib3(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        print(b)
        tmp = a
        a = b
        b = tmp + b    #b才是a+b
        n = n + 1
    return 'done'

print(fib3(7))    
    
