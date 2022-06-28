# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 03:00:44 2021

@author: ACER PREDATOR
"""

data=input().split(" ")
cha="00 01 100 101 1100 1101 11100 11101 111100 111101".split(" ")
word="DEFGHIJKLMNOPQRSTUVWXYZABC"
ans = ""
for i in range(0,len(data)):
    ans=ans + str(cha.index(data[i]))
print(word[int(ans)-1])
