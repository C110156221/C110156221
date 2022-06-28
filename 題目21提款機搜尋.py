# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 08:15:35 2020

@author: ACER PREDATOR
"""

n=int(input("輸入查詢組數N為："))
dict1={"123 456":"9000","456 789":"5000","789 888":"6000",
       "336 558":"10000","775 666":"12000","566 221":"7000"}

for i in range(1,n+1):
    data1=input("輸入帳號密碼(空白間隔開)：")
    if data1 in dict1:
        print(dict1[data1])
    else:
        print("error")
    