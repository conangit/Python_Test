#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['lihong', 'yaya', 'hanmei', 'is', 'll']
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

print(range(10))
print(list(range(2,10)))


###########################################

print(L[0:2])
print(L[3:4])

print(L[-3:-1])

L = list(range(100))
#print(L)

print(L[:10])
print(L[-10:])
print(L[11:21])

print(L[0:10:3])
print(L[::10])

l = L[:]
print(l)

##########################################

tp = (1,2,6,8,0)

print(tp[:])
print(tp[:3])
print(tp[2:3])    #(6,)

##########################################

s = 'lihong, you are a fool !'
print(s[0:6])
print(s[8:])







