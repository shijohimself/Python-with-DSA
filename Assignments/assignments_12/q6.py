L1 = [10,20,30,-10,1,9]
L2 = [10,23,8,12,7,73]

def addition(lst1,lst2):
    L1 = lst1
    L2 = lst2
    L3 = []
    n = len(L1)
    for i in range(0,n):
        total = L1[i] + L2[i]
        L3.append(total)
    return L3

print(addition(L1,L2))