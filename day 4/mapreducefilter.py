import functools
from unittest import result


l=[1,2,3,4,5,6,7,8,9]
numbers =(1,2,3,4)
def func(x):
    if x >= 2:
        print (x)
def add(n):
    return n*n

l2=filter(func , l)
p=tuple(l2)
print (p)
print(functools.reduce(lambda a,b: a if a>b else b ,l))
result = map(add,numbers)
print(list(result))