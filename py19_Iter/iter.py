#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from collections import Iterable
from collections import Iterator

print(isinstance('abc',Iterable))
print(isinstance([1, 2],Iterable))
print(isinstance((1, 2),Iterable))
print(isinstance({'a':1, 'b':2},Iterable))
print(isinstance(set([1, 2]),Iterable))

print(isinstance(100,Iterable))

print(isinstance( (i * i for i in range(1, 4)), Iterable))


print('##########')


print(isinstance('abc',Iterator))
print(isinstance([1, 2],Iterator))
print(isinstance((1, 2),Iterator))
print(isinstance({'a':1, 'b':2},Iterator))
print(isinstance(set([1, 2]),Iterator))

print(isinstance(100,Iterator))

print(isinstance( (i * i for i in range(1, 4)), Iterator))

print('##########')

def func():
    n = 1
    yield n
    n = n + 1

f = func()
print(isinstance(f, Iterable))
print(isinstance(f, Iterator))

print('##########')

L = [1, 2, 3, 4]
it = iter(L)

while True:
    try:
        v = next(it)
        print(v)
    except StopIteration as e:
        print(e.value)
        break












