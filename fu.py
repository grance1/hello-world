#!/usr/bin/python2.7
>>> str(123)
'123'
>>> str(1.23)
'1.23'
print int('123')
print int(12.34)
print str(123)
print str(1.23)
print str('1.23')
from math import fsum
L = []
# print L
L=list(map(lambda x: x*x,range(1,101)))
print sum(L)

L = range(1,101)
