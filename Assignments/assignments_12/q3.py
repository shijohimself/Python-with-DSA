L = []
for i in range(1,11):
    n = int(input(f"Enter num {i} = "))
    L.append(n)

n = len(L)
result = []
for i in range(0,n-1):
    if L[i] % 2 != 0:
        result.append(L[i])
print(result)
