# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:46:33 2020

@author: 91842
"""
s = input()
m = 0
d = []
for char in s:
    if char in d:
        d = d[d.index(char)+1:]
        
        
    d.append(char)
    print(d)
    
    m = max(m, len(d))

print(m)