# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 07:29:07 2020

@author: ACER PREDATOR
"""

data1=input("請輸入一字元為：")
data2=data1[-1::-1]
if data1 == data2:
    print("YES")
else:
    print("NO")