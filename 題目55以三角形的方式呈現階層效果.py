
data1=int(input("請輸入一個正整數(限制10以下):"))
for i in range(1,data1+1):
  for j in range(1,i+1):
    data2=i*j
    print("%2d" %(data2),end=" ")
  print()
