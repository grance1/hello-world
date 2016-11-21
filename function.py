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
def greet(name='world'):
        print 'Hello,'+ name+'.'
print greet()
print greet('Bart')
import math
def move(x,y,step,angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x , y = move(100,100,60,math.pi/6)
print x , y
r = move(100,100,60,math.pi/6)
print r

import math
def quadratic_equation(a,b,c):
    if math.sqrt(b *b -4*a*c) >= 0:
        return (-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)
    else:
        return "none"
print quadratic_equation(2,3,1)
print quadratic_equation(1,3,-4)

