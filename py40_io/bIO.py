#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO

'''
f = BytesIO()
ret = f.write('中文'.encode('utf-8'))
print(ret)
print(f.getvalue())
'''


f = BytesIO(b'\xe4\xff\xc9')
print(f.read())


