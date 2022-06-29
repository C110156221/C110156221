
rows = int(input('输入列数： '))
i = j = k = 1
for i in range(rows):
    for j in range(rows - i):
        print(" ", end="")
        j += 1
    for k in range(2 * i - 1):
        print("*", end="")
    print ("")
for i in range(rows):
    for j in range(i):
        print(" ", end="")
        j += 1
    for k in range(2 * (rows - i) - 1):
        print("*", end="")
    print("")
    i += 1
