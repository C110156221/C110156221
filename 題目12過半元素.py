# -*- coding: utf-8 -*-
"""
@author: 陳劭
"""

n = input("輸入一整數序列為:").split(" ")
l1=[]
for i in range(len(n)):
    c=n.count((n[i]))
    l1.append(c)
m=max(l1)
if m>(len(n)/2):    
    a = l1.index(m)
    print("過半元素為:"+n[a])
else:
    print("過半元素為:NO")
