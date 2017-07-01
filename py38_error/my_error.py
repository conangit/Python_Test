#!/usr/bin/env python3
# -*-coding: utf-8 -*-
import logging

'''
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')


try:
    print('try...')
    #r = 10 / int('a')
    #r = 10 / 0
    r = 10 / 4
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error:')
finally:
    print('finally...')
'''
'''
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
'''

'''
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('4')
foo('0')
'''

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value:%s' % s)
    return 10 / n

def bar(s):
    try:
        foo(s)
    except ValueError as e:
        print("ValueError")
        raise

def main():
    try:
        bar('0')
    except ValueError as e:
        print('Error:%s' % e)

main()

'''
和C++错误处理机制类似
'''