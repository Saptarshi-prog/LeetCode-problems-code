# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 20:17:38 2020

@author: Saptarshi
"""



str = input()
num = '0'
sign = ''
        
str = str.lstrip()
print(str)
        
if not str:
    print(int(num))
        
if str[0] in ['-', '+']:
    sign = str[0]
    str = str[1:]
            
for c in str:
    if c.isdigit():
        num += c
    else:
        break
        
if sign and int(num):
    num = sign + num

if int(num) < 0:
    print(max(int(num), -2147483648))
else:
    print(min(int(num), 2147483647))
