n = int(input("enter a value = "))
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j , end = " ")
    print()