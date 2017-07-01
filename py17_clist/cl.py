#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

l = list(range(1, 11))
print(l)

l = []
for i in range(1,11):
    l.append(i)
print(l)

l = []
for i in range(1,11):
    l.append(i * i)
print(l)

l = [i for i in range(1,11)]
print(l)

l = [i * 2 for i in range(1,11)]
print(l)

l = [i for i in range(1,20) if i % 3 == 0]
print(l)

l = [i+j for i in 'abc' for j in '123']
print(l)

L = [d for d in os.listdir('.')]
print(L)


dc = {'a':'AA', 'b':'BB', 'c':'CC'}
l = [k + '=' + v for k, v in dc.items()]    # 顺序可能不一样哦
print(dc)
print(l)

L = ['AA', 'BB', 'Microsoft', 'Apple']
l = [s.lower() for s in L]
print(l)


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)


