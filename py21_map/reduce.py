#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from functools import reduce

# reduce(f, [x1, x2, x3]) = f(f(f(x1, x2), x3), x4)
# reduce示例一
def f(x1, x2):
    return x1 * x2

L = [1, 2, 3, 4, 5]
print(reduce(f, L))

print('###############################')

def fn(x, y):
    return x *10 + y

L = [1, 2, 3]
print(reduce(fn, L))

def str2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

print(list(map(str2num, '1356')))
print(reduce(fn, map(str2num, '1356')))

print('###############################')

def str2int(s):
    def str2num(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(str2num, s))

s1 = '124078'
print(str2int(s1))

print('###############################')

def str2num(s):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(str2num, s))

print(str2int('3456'))

print('###############################')

L1 = ['LIhonG', 'GSD', 'HkFF', 'aabb']

def normalize(s):
    #return s.lower()
    #return s.capitalize()
    return s[0:1].upper() + s[1:].lower()

L2 = list(map(normalize, L1))
print(L2)

print('###############################')

L = [2, 3, 4, 5]
print(sum(L))

def prod(l):
    def f(x, y):
        return x * y
    return reduce(f, l)

print(prod(L))

print('###############################')

def str2float_1(s):
    def str2num(s):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

    def fn(x, y):
        return x * 10 + y                   # 以上为str2int部分
        
    for i, v in enumerate(s):
        if(v == '.'):                       # 取得字符串小数点下标
            break
        
    s1 = s[0:i]                             # 分离字符串整数和小数部分
    s2 = s[i+1:]

    r1 = reduce(fn, map(str2num, s1))       # 字符串转化为整数
    r2 = reduce(fn, map(str2num, s2))

    i = 0
    while i < len(s2):                      # 计算小数部分
        r2 = r2 * 0.1
        i = i + 1

    return r1 + r2                          # 数据合成
        
    
print(str2float_1('12.567'))
print(str2float_1('1.1'))
#print(str2float('123'))    #bug
print('12.567 * 1.1 = ', str2float_1('12.567') * str2float_1('1.1'))    # 验证
#print('12.567' * '1.1')

print('###############################')

print(float('12.567'))
print(float('1.1'))
print(float('123'))
print(float('12.567') * float('1.1'))

print('###############################')

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1,
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('12.567'))
print(str2float('1.1'))
print(str2float('123'))
print('12.567 * 1.1 = ', str2float('12.567') * str2float('1.1'))    # 验证



    
