#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import functools

def log(func):
    def wrapper(*args, **kw):                   # 可变参数 关键字参数
        print('call %s():' %func.__name__)      # 打印日志
        return func(*args, **kw)                # 返回原始函数
    return wrapper

@log
def now():
    print('2017-4-6')
    return 'ok'

print(now())

@log
def add(i , j):
    return i + j

print(add(3, 4))
print(add.__name__)

print("####")

def mylog(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@mylog('lihong\'s func')
def sum(i , j):
    return i + j

print(sum(1, 2))
print(sum.__name__)    # wrapper

print("####")

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('Begin %s %s():' %(text, func.__name__))
            ret = func(*args, **kw)
            print('End %s %s():' %(text, func.__name__))
            return ret
        return wrapper
    return decorator

@log2('exec')
def my_f(i , j):
    return i + j

print(my_f(1, 2))
print(my_f.__name__)
