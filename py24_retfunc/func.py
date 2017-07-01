#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax          # 得到计算结果后返回

print(calc_sum(1, 2, 3, 4))
print(calc_sum(1, 2, 3, 4, 5))

print('####')

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum                  # 返回参数求和函数，并未立即执行

f1 = lazy_sum(1, 2, 3, 4 ,50)   # f1 = SUM(1, 2, 3, 4 ,50) = 产生求和函数f1,调用得到结果
f2 = lazy_sum(3, 4, 5)          # f2 = SUM(3, 4, 5) = 产生求和函数f2,调用得到结果
print(f1())
print(f2())

print('####')

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)    # 函数并没有立即执行，得到函数f(i * i)
    return fs

#print(count())    # 可以看出产生了一个函数序列

f1, f2, f3 = count()    # 序列赋值运算
print(f1(), f2(), f3())

# 返回函数均引用了变量i，但是函数并没有立即执行，即
# [f1(i * i), f2(i * i), f3(i * i)]
# 三个函数都返回时，i此时变为3，故返回都为9

def count():
    def f(j):
        def g():
            return j * j
        return g           # 返回函数f(j * j),不立即执行
    fs = []
    for i in range(1, 4):
        fs.append(f(i))    # i的当前值被传入f(i),f(i)立即执行,得到f(i)计算结果
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

'''
总结：
1.返回闭包时，返回函数不要引用任何循环变量，或者后续会发生改变的标量
2.返回一个函数时，函数并未立即执行，调用函数才得以执行
'''