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
