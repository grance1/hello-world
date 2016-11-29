#!/usr/bin/python2.7
>>> import re
>>> re.match(r'^\d{3}\-\d{3,8}$','010-12345')
<_sre.SRE_Match object at 0x7fcbcde72988>
>>> re.match(r'^\d{3}\-\d{3,8}$','010 12345')
import re
test = '用户输入的字符串'
if re.match(r'正则表达式',test):
    print('ok')
else:
    print('failed')


>>> 'a b  c'.split('')
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: empty separator
>>> re.split(r'\s+','a b  c')
['a', 'b', 'c']
>>> re.split(r'[\s\,]+','a,b,c d')
['a', 'b', 'c', 'd']
>>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object at 0x7fcbcde5c2d8>
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'
>>> t = '19:05:30'
>>> m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
>>> m.group()
'19:05:30'
>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')


