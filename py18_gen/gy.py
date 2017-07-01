def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 3 
    print("step 3")
    yield 5

o = odd()        #generator对象
print(next(o))
print(next(o))
print(next(o))

print('######')

#generator函数，每次调用next()时候执行，遇到yield返回，再次执行时从上次返回的yield处继续

def fib(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        yield b
        tmp = a
        a = b
        b = tmp + b
        n = n + 1
    return 'done'

for n in fib(5):
    print(n)




        

