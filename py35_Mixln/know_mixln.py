#!/usr/bin/env python3
# -*-coding: utf-8 -*-

class A(object):
    def pfA(self):
        print('A')

class B(A):
    def pfB(self):
        print('B')

class C(object):
    def pfC(self):
        print('C')

class D(B, C):
    def pfD(self):
        print('D')

d = D()
d.pfD()
d.pfB()
d.pfC()
d.pfA()
