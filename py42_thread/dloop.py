#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import multiprocessing

def loop():
	x = 0
	while True:
		x = x ^ 1

for i in range(multiprocessing.cpu_count()):
	t = threading.Thread(target = loop)
	t.start()

# New Terninal
# top 
# 102%