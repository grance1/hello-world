#!/usr/bin/python2.7
print abs(100)
print abs(-20)
print abs(12.34)
print cmp(1,2)
print cmp(2,1)
print cmp(3,3)
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
#print L
#for x in L:
print sum(x*x for x in L)
