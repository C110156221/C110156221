
dict1 = {}
n = int(input("請輸入n值："))
for i in range (1,n+1):
    data1=input("請輸入姓名：")
    data2=input("請輸入電子郵件：")
    dict1[data1] = data2
data3=input("請輸入查詢電子郵件的姓名：")
if data3 in dict1:
    print(data3+" 電子郵件帳號為 "+dict1[data3])
