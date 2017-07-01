#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 知识点一
ll = list(range(5))
print(ll)
print(len(ll))
print('####')

# 知识点二
L1 = [1, 3]
L2 = [4]
L3 = ['a', 'b', 'c']
L4 = L1 + L2 + L3
L5 = [L1[0] + L1[1]]
print(L4)
print(L5)
print('####')

# 知识点三
T = [i * i for i in range(3)]
print(T)
print('####')

# 知识点四
l = list(range(1,1))
print(l)

print('Begin')
for i in range(1, 1):
    print(i)
    l = []
    l[i] = l[i] + [i-1]
    print(l)
print('Stop')

print('####')

def triangles1():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1] + L[i] for i in range(len(L))]    # 列表生成式
        #print('L:', L)

def triangles2():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]    # i == None ?
        ret.append(1)
        pre = ret[:]
    



n = 0
for t in triangles1():
    print(t)
    n = n + 1
    if n == 10:
        break
    
print('####')

n = 0
for t in triangles2():
    print(t)
    n = n + 1
    if n == 10:
        break



