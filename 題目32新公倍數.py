
data1=int(input("輸入一正整數："))
data2=data1%2
data3=data1%11
data4=data1%5
data5=data1%7
if data2==0 and data3==0:
    if data4!=0 and data5!=0:
        print("%d為新公倍數？：YES" %(data1))
    else:
        print("%d為新公倍數？：NO" %(data1))
else:
    print("%d為新公倍數？：NO" %(data1))
