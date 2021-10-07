# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:33:51 2020

@author: Saptarshi Neogi
"""

a = int(input())

c = a
        
if a<0:
    a=-a
    
d = list(str(a))
b = []
i = len(d)-1
        
while i>=0:
    b.append(d[i])
    i-=1
            
ans = "".join(map(str,b))
ans = int(ans)
        
if c<0:
    ans= -ans
            
if ans > (2**31-1) or ans<-(2**31):
    print(0)
else:
    print(ans)
