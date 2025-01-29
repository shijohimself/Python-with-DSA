L = []
for i in range(1,11):
    n = int(input(f"enter num {i} = "))
    L.append(n)
print(L)

L2 = []
n = len(L)
for i in range(n - 1 ,-1,-1):
    L2.append(L[i])
print(L2)