#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('abc'.encode('ascii'))
#print('����'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('abc'))
#print(len('�й�'))

print(len(b'abc'))
#print(len('�й�'.encode('utf-8')))
