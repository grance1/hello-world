#!/usr/bin/python2.7
L = [75,98,59,81,66,43,69,85]
sum = 0.0
n = 0
for x in L:
    sum = sum + x
    n = n + 1
print sum / n

L = [75,98,59,81,66,43,69,85]
sum = 0.0
n = 0
for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
print sum / n

sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum = sum + x
print sum
for x in L:
    if x < 60:
        continue
    sum = sum + x
    n = n + 1
print sum / n
