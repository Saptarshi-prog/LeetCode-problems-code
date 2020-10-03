# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:06:38 2020

@author: 91842
"""
hour,minutes = [int(i) for i in input().split()]

a=hour+minutes/60
b = minutes/5

c = max(a,b)
d = min(a,b)
        
ans = (c-d)*30
ans1 = 360-ans
ans2 = min(ans,ans1)
print(ans2)
