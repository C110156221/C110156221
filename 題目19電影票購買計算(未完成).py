
n=int(input("請輸入組數："))
list1=[]
for i in range(1,n+1):
    data1,data2 = int(input("第%d組：" %(i)).split(" "))
    list1[data1] = data2
