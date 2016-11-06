#!/usr/bin/python
a=['list','tuple','function']
print a
>>> aList=[3,5,7]
>>> bList=aList
>>> id(aList)
140137226622808
>>> aList=aList*3
>>> aList
[3, 5, 7, 3, 5, 7, 3, 5, 7]
>>> bList
[3, 5, 7]
>>> id(aList)
140137226646448
>>> id(bList)
140137226622808
>>> x=[[None] *2 ] * 3
>>> x
[[None, None], [None, None], [None, None]]
>>> x[0][0]=5
>>> x
[[5, None], [5, None], [5, None]]
>>> x=[[1,2,3]] *3
>>> x
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
>>> x[0][0]=10
>>> x
[[10, 2, 3], [10, 2, 3], [10, 2, 3]]
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> xrange(10)
xrange(10)
>>> list(xrange(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=[3,4,5]
>>> a.append(7)
>>> a
[3, 4, 5, 7]
>>> a.insert(3,6)
>>> a
[3, 4, 5, 6, 7]
>>> a=[1,2,3,4]
>>> a
[1, 2, 3, 4]
>>> a=1,
>>> a
(1,)
>>> id(a)
140644191493968
>>> b=a
>>> id(b)
140644191493968
>>> c=2
>>> d=3
>>> c+d
5
>>> id(c)
24596800
>>> L
['Adam', 'Lisa', 'Paul']
>>> L[-1]
'Paul'
>>> L[0]='Bart'
>>> L
['Bart', 'Lisa', 'Paul']
>>> L[-1]='Adam'
>>> L
['Bart', 'Lisa', 'Adam']


