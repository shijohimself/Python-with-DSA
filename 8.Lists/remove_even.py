# remove even

L = [2,5,6,8,9,10,5,6,4]

# never change the length of list
result = []
n = len(L)

for i in range(0,n):
    if L[i] % 2 != 0:
        result.append(L[i])
print(result)