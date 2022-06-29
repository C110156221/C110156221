
data1=input("輸入一組四位數字：")
l1=list(map(int,data1))

a=((l1[0]+7)%10)
b=((l1[1]+7)%10)
c=((l1[2]+7)%10)
d=((l1[3]+7)%10)

print(c,d,a,b)


