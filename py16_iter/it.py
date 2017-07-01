#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

d = {'a':11, 'b':22, 'c':33}

#迭代结果顺序可能不一样
for k in d:
    print(k)

for v in d.values():
    print(v)
  
for k, v in d.items():
    print(k, v)
    

s = 'abc'
for ch in s:
    print(ch)
    

print(isinstance('abc', Iterable))
print(isinstance('[1,2,3]', Iterable))
print(isinstance('(1,2,3)', Iterable))
print(isinstance('{\'a\':1, \'b\':2}', Iterable))
print(isinstance('set([1,2,3])', Iterable))

st = set([34, 6, 78])
for t in st:
    print(st)

L = ['a', 'b', 18, 19, 'aa']
for v in L:
    print(v)
  
for i, v in enumerate(L):
    print(i, v)
    
    





