# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 03:59:07 2020

@author: ACER PREDATOR
"""

dict1 = {}

n = int(input("請輸入n值："))
for i in range (1,n+1):
    data1=input("請輸入獎牌種類：")
    data2=input("請輸入獎牌數量：")
    dict1[data1] = data2
item1 = list(dict1.items())
for n1, n2 in item1:
    print("%s牌得到 %s 面" %(n1,n2))
