#!/usr/bin/env python3
# -*-coding: utf-8 -*-

# __str__
class Std(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Std object (name: %s)' % self.name
    __repr__ = __str__

print(Std('Hello'))
s = Std('World')
print(s)

# __iter__ __getitem__
class Fib(object):
    def __init__(self):
        self.a, self.b = 1, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for i in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a, b = b, a+b
            return L

fib = Fib()

for n in fib:
    if n < 100:
        print(n, end=' ')
    else:
        break

print('\r')
print(fib[0])
print(fib[1])
print(fib[2])
print(fib[7])
print(fib[9])

print(fib[:10])

# __getattr__
class A(object):
    def __getattr__(self, attr):

        if attr == 'name':
            @property
            def name(self):
                return self._name
            @name.setter
            def name(self, val):
                self._name = val

        else:
            raise AttributeError('\'Object\' has no sttribute \'%s\'' % attr)

a = A()
a.name = 'lihong'
print(a.name)
#a.age

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s %s' % (self._path, path))

    def __str__(self):
        return self._path
    __repr__ = __str__

c = Chain('www.baidu.com')
c.name = 'll'
print(c.name)

# __call__
class Scall(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return 'My name is %s.' % self.name

sc = Scall('Hanmei')
print(sc())

print(callable(Scall))
print(callable(sc))
print(callable([1, 2]))
