
data1=int(input("請輸入第一個要判斷的數字："))
data2=int(input("請輸入第二個要判斷的數字："))
data3 = data1 % 2
data4 = data2 % 2
if data3 == 0 or data4 == 0:
    print("N")
else:
    print("Y")
