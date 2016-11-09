#!/usr/bin/python2.7
import math
sum = 0
x = 1
n = 1
while True:
   sum = sum + n
   n = pow(2,x)
   x = x + 1
   if x > 19:
       break
print sum
    

