#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io

'''
f = open('./tmp.txt', 'r')
print(f.read())
'''

'''
try:
	f = open('./tmp.txt', 'r')
	print(f.read())
finally:
	f.close()
'''

'''
with open('./tmp.txt', 'r') as f:
	print(f.read())
'''

'''
with open('./tmp.txt', 'r') as f:
	#print(f.readline())
	#print(f.readline())
	print(f.read(15))
'''

'''
with open('./tmp.txt', 'r') as f:
	for line in f.readlines():
		print(line.strip())
'''

'''
with open('./kf.jpg', 'rb') as p:
	print(p.read())
'''

with open('./tmp.txt', 'w') as f:
	f.write('i am lihong')

with open('./tmp.txt', 'r') as f:
	print(f.read())


