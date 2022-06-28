# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 02:39:26 2021

@author: ACER PREDATOR
"""

def gcd(a,b):
    if b==0:
        return a
    else:   
        c=a%b
        return gcd(b,c)

data=input().split(",")
ans=[]
for i in range(0,len(data)-1):
    for j in range(i+1,len(data)):
        ans.append(gcd(int(data[i]),int(data[j])))
print(max(ans))
