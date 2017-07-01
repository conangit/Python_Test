#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def f(x):
    return x * x

L = [1, 2, 3, 4, 5]
r = map(f, L)

print(r)
print(list(r))
#or
for n in r:
    print(n)

s = []
for n in L:
    s.append(f(n))
print(s)

print(list(map(str, [1, 2, 3, 4, 5])))
