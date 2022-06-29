

data1=input("檢測的字串(end結束)：")
data2=input("檢測的單一字元：")
while (data1 != "end"):
    print("字元%s出現的次數為：%d" %(data2,data1.count(data2)))
    data1=input("檢測的字串(end結束)：")
    if data1 == "end":
        break
    data2=input("檢測的單一字元：")
    
print("檢測結束")
