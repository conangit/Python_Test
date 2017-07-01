#!/usr/bin/env python3
# -*-coding: utf-8 -*-


print(dir(list))

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)

# --- ORM ---
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Fount modle: %s' % name)

        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings   # 保存属性和列的映射关系
        attrs['__table__'] = name          # 假设表名和类名一致

        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=123456, name='Lihong', email='li@gzseeing.com', password='hello')
u.save()


'''
__new__()
cls -- 当前准备创建的类的对象
name -- 类的名字
bases -- 类继承的父类集合
attrs -- 类的方法集合

__new__ : 类级别方法
__init__ : 实例级别的方法
'''

'''
一些理解：
流程上：先定义metaclass,然后创建类,再创建类的实例
元类：创建类的类,是一个类的创建工厂
type:type就是一个元类，可以用它去创建类
'''

'''
class Child(Father):
    pass
Python类的创建过程：
Child是否有__metaclass__属性，有通过此创建类的对象，无，上一级寻找
Facher是否有__metaclass__属性，有通过此创建类的对象，都无
在模块中寻找__metaclass__,还是无
用type创建

自定义元类：
    拦截类的创建，修改一些特性，然后返回该类。（有那么一丁点类似装饰器）
'''