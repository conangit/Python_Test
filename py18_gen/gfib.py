#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max :
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(3)
print(f)
print(next(f))
print(next(f))
print(next(f))


for n in f:
    print(n)


