#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Lihong' : 100, 'Yaya' : 90, 'Hnamei' : 80}
print(d['Lihong'])

d = {1 : 'Lihong', 2 : 'Yaya', 3 : 'Hnamei'}
print(d[2])

d = {1 : 'Lihong', 2 : 'Yaya', 3 : 'Hnamei'}
d[2] = 'LaoWang'
print(d[2])
#print(d[5])

print(d.get(5, 'SB'))
#print(d[5])  #??
print(d)	

d.pop(2)
print(d)

L = [1, 3]
#L = [1, 2]
#print(d[L])
print(d[L[0]])
print(d[L[1]])




