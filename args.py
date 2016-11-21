#!/usr/bin/python2.7
def fn(*args):
    print args
print fn()
print fn('a')
print fn('a','b')
print fn('a','b','c')

def aversge(*args):
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print aversge()
print aversge(1,2)
print aversge(1,2,2,3,4)

