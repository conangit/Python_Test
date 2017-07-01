#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO


'''
f = StringIO()
f.write('hello')
print(f.getvalue())
'''

f = StringIO('i\n love\n you')
while True:
	s = f.readline()
	if s == '':
		break
	#print(s)
	print(s.strip())

