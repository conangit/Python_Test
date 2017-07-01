#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny

r = move(0, 0, 1.414, 3.1415926/4)
print(r)
	

