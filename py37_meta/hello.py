#!/usr/bin/env python3
# -*-coding: utf-8 -*-

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s' % name)


#CPython看到的类定义
#Hello = type('Hello', (object,), dict(hello = hello))