
dict1 = {}
n = int(input("請輸入n值："))
for i in range (1,n+1):
    data1=input("請輸入英文：")
    data2=input("請輸入中文：")
    dict1[data1] = data2
data3=input("請輸入查詢單字：")
if data3 in dict1:
    print(data3+" 中文意思 "+dict1[data3])
else:
    print("字典未有此單字")
