
a = int(input("請輸入十進位的正整數："))
b=a
ans=""
while b//3 != 0:
    ans=str(b%3)+ans
    b=b//3
ans = int(str(b)+ans)
print("%d的三進位為%d" %(a,ans))
