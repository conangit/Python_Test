#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


#print(os.name)
#print(os.uname())

#print(os.environ)
#print(os.environ.get('PATH'))


print(os.path.abspath('.'))
print(os.path.join('.', 'tmp'))
os.mkdir('./tmp')
os.rmdir('./tmp')

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
