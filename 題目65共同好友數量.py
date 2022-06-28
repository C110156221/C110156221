# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 02:37:47 2021

@author: ACER PREDATOR
"""

a=input("請輸入A的好友:").split(" ")
b=input("請輸入B的好友:").split(" ")
ans =0
for i in range(0,len(a)):
    if a[i] in b:
        ans+=1
print(ans)
