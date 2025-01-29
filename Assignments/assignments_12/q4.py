L = [1,5,7,1,1,1,9,2,1,4,6,2,1,0,10,212,121,9,89,73]
result = []
n = len(L)
for i in range(0,n-1):
    if L.count(L[i]) > 3:
        if L[i] not in result:
            result.append(L[i])
print(result)

