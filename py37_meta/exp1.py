#!/usr/bin/env python3
# -*-coding: utf-8 -*-

print( type('trick', (), {}) )      #类
print( type('trick', (), {})() )   #类的实例



class Father(object):
    pass

Child = type('Child', (Father,), {'laugh_at': 'haha'})

print( Child().laugh_at )
print( Child.__dict__ )
print( Child.__base__ )
print( Child.__bases__ )
print( Child().__class__ )
print( Child().__class__.__class__ )

class FatherMetaclass(type):
    def __new__(cls, class_name, class_parents, class_attr):
        attrs = ( (name, value) for name, value in class_attr.items() if not name.startswith('__'))
        class_attr = dict((name.upper(), value) for name, value in attrs)
        return type.__new__(cls,class_name, class_parents, class_attr)

class Ch(object, metaclass=FatherMetaclass):
    bar = 12
    money = 'meiyuan'

print(Ch.BAR)
print(Ch.MONEY)

class AuthorTagMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['author'] = 'Lihong'
        attrs['getname'] = lambda self: self.__class__
        return type.__new__(cls, name, bases, attrs)

class LH(object, metaclass=AuthorTagMetaclass):
    pass

#print(dir(LH))

lh = LH()
print(lh.author)
print(lh.getname())