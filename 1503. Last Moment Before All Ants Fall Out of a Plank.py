# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 13:55:23 2020

@author: 91842
"""
def getLastMoment(n,left,right):
        ans=0

        for x in right:
            ans=max(n-x,ans)
        
        for x in left:
            ans=max(x,ans)
    
        return ans
    
print(getLastMoment(4, [4,3], [0,1]))