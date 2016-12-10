#!/usr/bin/python2.7
import datetime                          
from datetime import datetime            
now = datetime.now()                     
print(now)                               
                                         
print(type(now))                         
from datetime import datetime            
dt = datetime(2015, 4, 19, 12, 20)       
print(dt)                                
                                         
from datetime import datetime            
t = 1429417200.0                         
print(datetime.fromtimestamp(t))         
                                         
from datetime import datetime            
t = 1429417200.0                         
print(datetime.fromtimestamp(t))         
print(datetime.utcfromtimestamp(t))      
                                         
from datetime import datetime            
cday = datetime.strptime('2015-6-1 18:19:
print(cday)                              
                                         
                                         
from datetime import datetime            
now = datetime.now()                     
print(now.strftime('%a, %b %d %H:%M'))   
from datetime import datetime, timedelta 
now = datetime.now()                     
print now                                
                                         
print now + timedelta(hours=10)          
print now - timedelta(days=1)            
print now + timedelta(days=2, hours=12)  
