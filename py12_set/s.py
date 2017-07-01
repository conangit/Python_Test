#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = set([3, 2, 3, 2, 1])
print(s)

s.add(4)
print(s)

s.remove(1)
print(s)

s1 = set([3, 4, 5])
print(s | s1)
print(s & s1)
