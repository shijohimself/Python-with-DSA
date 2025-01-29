L = [1,4,6,7,4,32,123,54,677,21,90,80,70,77,57]
L_odd = []
L_even = []

n = len(L)
for i in range(0,n):
    if L[i]% 2 == 0:
        L_even.append(L[i])
    else:
        L_odd.append(L[i])
print(L)
print(L_odd)
print(L_even)
