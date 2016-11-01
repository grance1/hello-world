#!/user/bin/python2.7
>>> L=['Adam','Lisa','Bart','Paul']
>>> L.pop()
'Paul'
>>> L
['Adam', 'Lisa', 'Bart']
>>> L=['Adam','Lisa','Paul','Bart']
>>> L.pop(2)
'Paul'
>>> ;
  File "<input>", line 1
    ;
    ^
SyntaxError: invalid syntax
>>> L
['Adam', 'Lisa', 'Bart']
>>> L.pop(2)
'Bart'
>>> L=['Adam','Lisa','Paul','Bart']
>>> L.pop(2)
'Paul'
>>> L.pop(2)
'Bart'
>>> L
['Adam', 'Lisa']
