#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

L = [1, 2, 3, 5, 6]
print(list(filter(is_odd, L)))

def not_empty(s):
    return s and s.strip()

S = ['A', ',', 'B', None, '78', '  ']
print(list(filter(not_empty, S)))

#埃式筛法
def n_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_div(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = n_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_div(n), it)

for n in primes():
    if n < 40:
        #print(n, end=" ")
        pass
    else:
        break

#埃式筛法
#自然数序列
def N_iter():
    n = 1
    while True:
        n = n + 1
        yield n

#求余判断
def N_div(n):
    return lambda x: x % n != 0

#生成素数列
def Primes():
    nL = N_iter()                        #初始化自然数序列[2, 3, 4, 5, 6, 7, 8, 9, ...]
    while True:
        n = next(nL)                    #取第一个数2
        nL = filter(N_div(n), nL)       #每个数与2求余，筛选得到新序列
        yield n

for i in Primes():
    if i < 50:
        print(i, end=' ')
        i = i + 1
    else:
        break

#回数问题
def is_palindrome(n):
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(1, 100))
print(list(output))
