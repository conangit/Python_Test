#!/usr/bin/env python3
# -*-coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)
import pdb


'''
def foo(n):
    assert n != 0, 'n is zero'
    return 10 / n

def main():
    try:
        foo(0)
    except AssertionError as e:
        print('AssertionError: %s' % e)

main()
'''

#python -O err.py 关闭assert运行程序


s = '0'
n = int(s)
#logging.info('n = %d' % n)
#pdb.set_trace()
print(10 / n)

