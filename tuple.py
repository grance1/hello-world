#!/usr/bin/python2.7
b=('2','tuple')
print b
>>> a_tuple=('a',)
>>> a_tuple
('a',)
>>> a_tuple=('a','b','mpilgrim','z','example')
>>> a_tuple
('a', 'b', 'mpilgrim', 'z', 'example')
>>> x=()
>>> x
()
>>> a=3
>>> a
3
>>> a=(3)
>>> a
3
>>> a=3,
>>> a
(3,)
>>> a=1,2
>>> a
(1, 2)
>>> t = ('Adam','Lisa','Bart')
>>> t
('Adam', 'Lisa', 'Bart')
>>> t[-1]
'Bart'
>>> t[0]='Paul'
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t=(0,1,2,3,4,5,6,7,8,9)
>>> t
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> t = ()
>>> t
()
>>> t = (1)
>>> t
1
>>> t = (1,)
>>> t
(1,)
>>> t=(1,2,3,)
>>> t
(1, 2, 3)
>>> t=('Adam')
>>> t
'Adam'
>>> t=('Adam',)
>>> t
('Adam',)
>>> t = ()
>>> t
()
>>> t = (1)
>>> t
1
>>> t = (1,)
>>> t
(1,)
>>> t=(1,2,3,)
>>> t
(1, 2, 3)
>>> t=('Adam')
>>> t
'Adam'
>>> t=('Adam',)
>>> t
('Adam',)
>>> t = ()
>>> t
()
>>> t=('a','b',['A','B'])
>>> t
('a', 'b', ['A', 'B'])
>>> L=t[2]
>>> L
['A', 'B']
>>> L[0]='X'
>>> L[1]='Y'
>>> t
('a', 'b', ['X', 'Y'])


