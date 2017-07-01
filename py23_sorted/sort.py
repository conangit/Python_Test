#!/usr/bin/env python3
#-*- coding: utf-8 -*-

L = sorted([1, 5, -7, 6, 4, 2])
print(L)

L = sorted([1, 5, -7, 6, 4, 2], key=abs)
print(L)

L = sorted(['ab', 'sample', 'Lihong', 'OK'])
print(L)

def str_change(s):
    #s = s.lower()
    s = s.upper()
    return s

L = sorted(['ab', 'sample', 'Lihong', 'OK'], key=str_change)
print(L)

L = sorted(['ab', 'sample', 'Lihong', 'OK'], key=str.upper)
print(L)

L = sorted(['ab', 'sample', 'Lihong', 'OK'], key=str.upper, reverse=True)
print(L)

L1 = [('Ya', 70), ('Hanmei', 86), ('lia', 69)]

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]

L2 = sorted(L1, key=by_name)
print(L2)

L3 = sorted(L1, key=by_score)
print(L3)

